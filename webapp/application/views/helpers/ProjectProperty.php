<?php

class Appdate_View_Helper_ProjectProperty extends Zend_View_Helper_Abstract {

  public function projectProperty($property) {
    
    if (empty($property))
      return "<span class='quiet'>unknown</span>";
    
    $output = $property;
    if (eregi('^http[s]?:\/\/|^ftp:\/\/', $property)) {
      $text = $this->view->escape($property);
      if (strlen($property) > 40) {
        $text = substr($property, 0, 40) . '&hellip;';
      }
      $text = "<a href='{$property}'><span title='{$property}'>{$text}</span></a>";
      
      $output = $text;
    }
    return $output;
  }

}
