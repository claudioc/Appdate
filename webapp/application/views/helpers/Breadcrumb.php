<?php
class Appdate_View_Helper_Breadcrumb extends Zend_View_Helper_Abstract {

  public function breadcrumb($path) {
    return "<a href='/'>Home</a> &raquo; {$path}";
  }

}


