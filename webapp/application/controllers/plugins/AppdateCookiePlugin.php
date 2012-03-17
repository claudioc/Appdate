<?php
class AppdateCookiePlugin extends Zend_Controller_Plugin_Abstract
{
  public function preDispatch(Zend_Controller_Request_Abstract $request) {
    if (isset($_COOKIE['APPDATE_SHELFID'])) {
      $shelfId = $_COOKIE['APPDATE_SHELFID'];
    } else {
      $shelfId = 0; 
    }
    if (!Shelf::isValidId($shelfId))
      $shelfId = 0;
    
    Zend_Registry::set('shelfId', $shelfId);
  }
}
