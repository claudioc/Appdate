<?php

Class Shelf extends Zend_Db_Table_Abstract {
  protected $_name='shelves';
  protected $_primary=array('id', 'projectName');
  static protected $_idGenerators = "23456789ABCDEFGHJKLMNOPQRSTUVWXYZ";
  
  const ACTION_ADDED = 1;
  const ACTION_REMOVED = 2;
  
  const ID_LENGTH = 10;
  
  const ORDER_ADDED_FIRST = 1;
  const ORDER_UPDATED_FIRST = 2;

  public static function storeId($id) {
    if (Shelf::isValidId($id)) {
      setcookie('APPDATE_SHELFID', $id, strtotime('2030-07-06'), "/");
      Zend_Registry::set('shelfId', $id);
    }
  }
  
  public function getShelfContent($id, $order=Shelf::ORDER_ADDED_FIRST, $includeSelf=FALSE) {

    $items = $this->fetchAll($this->select()
                                  ->where('id=?', $id)
                                  ->order('addedAt desc'));

    $projects = array();
    $model = new Project();
    foreach($items as $item) {
      $projects[] = $model->findByName($item->projectName);
      if ($item->projectName == 'Appdate')
        $includeSelf = FALSE;
    }

    if ($includeSelf) {
      $projects[] = $model->findByName('Appdate');
    }

    if (Shelf::ORDER_UPDATED_FIRST == $order)
      usort($projects, array('Project', 'projectsCmpByHistoryDate'));

    return $projects;
  }
  
  # Test if an Id exists in the db
  public function idExists($id) {
    return $this->fetchRow($this->select()->where('id=?', $id));
  }
  
  # Add or remove a project from a shelf
  public function toggleProject($id, $project) {
    if (!$this->isValidId($id))
      return;
    
    $name = is_object($project) ? $project->name : $project;
    
    if ($row = $this->fetchRow($this->select()
                                    ->where('id=?', $id)
                                    ->where('projectName=?', $name))) {
      $row->delete();
      return Shelf::ACTION_REMOVED;
    } else {
      $row = $this->createRow();
      $row->projectName = $name;
      $row->id = $id;
      $row->save();
      return Shelf::ACTION_ADDED;
    }
  }

  public function purge($id) {
    if ($this->isValidId($id))
      $this->delete("id='{$id}'");
  }
  
  public function generateId() {
    do {
      $id='';
      for ($x=0; $x < Shelf::ID_LENGTH; $x++) {
        $id .= Shelf::$_idGenerators[rand(0, strlen(Shelf::$_idGenerators) - 1)];
      }
      $row = $this->fetchRow($this->select()->where('id=?', $id));
    } while($row);
    return $id;
  }
  
  public static function isValidId($id) {
    $l=Shelf::ID_LENGTH;
    return ereg("^[A-Z0-9]{{$l}}$", $id);
  }
}


