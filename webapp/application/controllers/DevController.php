<?php

class DevController extends Zend_Controller_Action {
  
  public function indexAction() {
    
    // Lists bots
    
    $model = new Bot();
    
    $this->view->bots = $model->fetchAll();
    
    
  }

  
  public function getbotAction() {
    
    $this->view->botName = $this->getRequest()->getParam('botname');
    
    $model = new Bot();
    
    $this->view->body = $model->fetch($this->view->botName);
    
  }
  
}


