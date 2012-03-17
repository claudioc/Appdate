<?php

Class Project extends Zend_Db_Table_Abstract {
  protected $_name='projects';
  protected $_primary = array('name','historyId');
  
  protected $_rowClass = 'Project_Row';
  
  /*
   * Get the list of projects as an indexed array of name and most 
   * recent history id
   */
  public function getProjectNames() {
    $select = $this->select()
                   ->from($this, array('distinct(name) as name', 'max(historyId) as historyId'))
                   ->group('name');
    $output = array();
    foreach ($this->fetchAll($select) as $project) {
      $output[] = array('name' => $project->name, 'historyId' => $project->historyId);
    }
    return $output;
  }

  /* 
   * Find the current instance of a project, given its name 
   */
  public function findByName($name) {
    $project = NULL;
    foreach($this->getProjectNames() as $projectName) {
      if ($projectName['name'] == $name) {
        $project = $projectName;
        break;
      }
    }
    
    return $project ? $this->getProjectInstance($name, $project['historyId']) : NULL;
  }
  
  /*
   * Return the project list ordered by latest update date
   */
  public function getRecentProjectsList($limit=null) {
    $projects = $this->getProjectNames();
   
    $output = array();
    foreach($projects as $project) {
      $output[] = $this->getProjectInstance($project['name'], $project['historyId']);
    }
    
    # Sort projects on history date
    if (!empty($output))
      usort($output, array('Project', 'projectsCmpByHistoryDate'));
    
    # NULL as the length parameter works like "to the end"
    return array_slice($output, 0, $limit ? $limit : null);
  }
  
  public function getProjectInstance($name, $historyId) {
    $data = $this->fetchRow($this->select()
                                 ->where('name=?',$name)
                                 ->where('historyId=?', $historyId));
    $this->decodeData($data);
    return $data;
  }
  
  public function getProjectHistory($name) {
    $output = array();
    $items = $this->fetchAll($this->select()
                                  ->where('name=?', $name)
                                  ->order('historyDate desc')
                                  ->setIntegrityCheck(false));
    foreach($items as $item) {
      $this->decodeData($item);
      $output[] = $item;
    }
    
    return $output;
  }

  /*
   * Search projects for $words, either in the name or the project data
   */
  public function search($words) {

    $projects = $this->getProjectNames();

    $output = array();
    foreach($projects as $project) {
      $data = $this->getProjectInstance($project['name'], $project['historyId']);
      $set = (array)$data->projectData;
      $set['name'] = $project['name'];
      foreach(array_keys($set) as $key) {
        $string = strtolower($set[$key]);
        # Skip URLs
        if (substr($string, 0, 5) == 'http:')
          continue;
        $found=FALSE;
        foreach($words as $word) {
          if (FALSE !== strpos($string, $word)) {
            $output[] = $data;
            $found=TRUE;
            break;
          }
        }
        if ($found)
          break;
      }
    }
    return $output;
  }
  
  private function decodeData(&$project) {
    $project->releaseData = json_decode($project->releaseData);
    $project->projectData = json_decode($project->projectData);
  }
  
  static public function projectsCmpByHistoryDate($a, $b) {
    $a = strtotime($a->historyDate);
    $b = strtotime($b->historyDate);
    if ($a == $b)
      return 0;
    return $a > $b ? -1 : 1;
  }
  
}


