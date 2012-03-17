<?php

class PagesController extends Zend_Controller_Action {
  
  public function indexAction() {
    $slug = $this->getRequest()->getParam('slug');
    $this->render("static/{$slug}");
  }

}


