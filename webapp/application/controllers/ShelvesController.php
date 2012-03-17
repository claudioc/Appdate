<?php

class ShelvesController extends Zend_Controller_Action {

  public function init()
  {
    $ajaxContext = $this->_helper->getHelper('AjaxContext');
    $ajaxContext->addActionContext('toggle', 'json')
                ->addActionContext('box', 'html')
                ->initContext();
                
    $getContext = $this->_helper->getHelper('contextSwitch');
    $getContext->addActionContext('get', 'xml')->initContext();
  }

  public function boxAction() {
    $layout = Zend_Layout::getMvcInstance()->disableLayout();
  }
  
  public function openAction() {
    # We have three cases here:
    # - a shelf id is passed from the form
    # - we have a shelf id in the registry (read from the cookie)
    # - we do not have a shelf id (create a new one)
    
    $model = new Shelf();
    
    if ($shelfId = $this->getRequest()->getParam('shelfId')) {
      if (!Shelf::isValidId($shelfId)) {
        $this->_helper->redirector->gotoUrl("/");
        exit;
      }
      if (!$model->idExists($shelfId)) {
        $this->_helper->redirector->gotoUrl("/");
        exit;
      }
      # A correct shelf id has been passed
      Shelf::storeId($shelfId);
    }
    else {
      # Test if we have a the shelf id in the cookie
      $shelfId = Zend_Registry::get('shelfId');
    }

    if (empty($shelfId)) {
      $shelfId = $model->generateId();
      $model->toggleProject($shelfId, 'Appdate');
      Shelf::storeId($shelfId);
    }

    $this->_helper->redirector->gotoUrl("/");
  }

  public function purgeAction() {
    $shelfId = Zend_Registry::get('shelfId');
    if (!empty($shelfId)) {
      $model = new Shelf();
      $model->purge($shelfId);
      setcookie ('APPDATE_SHELFID', '0', time() - 3600, '/');
      Zend_Registry::set('shelfId', 0);
    }
    $this->_helper->redirector->gotoUrl("/");
  }
  
  # Show the list of your shelf (the order items are displayed changes with format)
  public function getAction() {
    $this->view->shelfId = $this->getRequest()->getParam('id');
    if (!Shelf::isValidId($this->view->shelfId))
      die();

    $outputIsRss = ('xml' == $this->getRequest()->getParam('format'));

    $model = new Shelf();
 
    # Always include appdate itself in xml format
    $this->view->projects = $model->getShelfContent($this->view->shelfId,
                                                    $outputIsRss ? Shelf::ORDER_UPDATED_FIRST : Shelf::ORDER_ADDED_FIRST,
                                                    $outputIsRss);

  }
  
  # Add or remove a project from the current shelf
  public function toggleAction() {
    $projectName = $this->getRequest()->getParam('projectName');
    
    $model = new Project();
    
    if ($project = $model->findByName($projectName)) {
      $model = new Shelf();
      $this->view->rc = $model->toggleProject(Zend_Registry::get('shelfId'), $project);
    } else {
      $this->view->rc = -1;
    }
  }

}


