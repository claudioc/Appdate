<?php

class SearchController extends Zend_Controller_Action {
  public function indexAction() {
    
    $this->view->q = $this->getRequest()->getParam('q');

    # Remove numbers from query (as people search "drupal 6"),
    # remove words less than 3 characters long and split $q in words
    $this->view->hasSearched=FALSE;
    if (strlen($this->view->q) > 2) {
      # Save search
      $model = new SearchLog();
      $search = $model->createRow();
      $search->query = $this->view->q;
      $search->client = $_SERVER['REMOTE_ADDR'];
      $search->save();
      
      $q = trim(preg_replace('/\b\w{,3}\b/','',preg_replace("/\d+/",'',$this->view->q)));
      if (!empty($q)) {
        $model = new Project();
        $this->view->hasSearched=TRUE;
        $this->view->projects = $model->search(split('[ ]+', $q));
      }
    }
    
  }

}


