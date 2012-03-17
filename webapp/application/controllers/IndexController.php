<?php

class IndexController extends Zend_Controller_Action {
  
  public function init()
  {
    $getContext = $this->_helper->getHelper('contextSwitch');
    $getContext->addActionContext('index', 'xml')->initContext();
  }
  
  public function indexAction() {
    $model = new Project();
    $limit = ('xml' == $this->getRequest()->getParam('format')) ? 10 : 0;
    $this->view->projects = $model->getRecentProjectsList($limit);
    $this->view->isFront = TRUE;
  }

  /*
  public function rssAction() {
   $model = new Project();

   $this->view->projects = $model->getRecentProjectsList();
   
   $entries = array();

   foreach($this->view->projects as $project) {
      $entries[] = array(
        'title'        => "{$project->name} - {$project->projectData->projectDescription}",
        'link'         => $project->projectData->projectWebSite,
        'guid'         => $project->releaseDataHash,
        'description'  => "Current release: {$project->releaseData->currentVersion}",
        'lastUpdate'   => strtotime($project->historyDate)
      );
    }
  
    $feeddata = array (
        'title'       => "Appdate.it",
        'description' => "The one stop software tracker",
        'link'        => "http://www.appdate.it",
        'author'      => "Claudio Cicali",
        'email'       => "claudio.cicali@appdate.it",
        'charset'     => 'UTF-8',
        'entries'     => $entries
        );
  
    $feed = Zend_Feed::importArray( $feeddata, 'rss' );
  
    $feed->saveXML();
    $feed->send();
    die();
  }
  */
  
}


