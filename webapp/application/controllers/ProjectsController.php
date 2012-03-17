<?php

class ProjectsController extends Zend_Controller_Action {
  
  public function historyAction() {
    
    require_once APPLICATION_PATH . '/models/Project.php';
    $model = new Project();

    $this->view->name = $this->getRequest()->getParam('name');
    
    $this->view->history = $model->getProjectHistory($this->view->name);
    $this->view->smash=123;
    
  }


}


