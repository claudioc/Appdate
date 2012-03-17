<?php
Class Project_Row extends Zend_Db_Table_Row {

  public function isInShelf() {
    static $response = array();
    
    if (!($shelfId = Zend_Registry::get('shelfId')))
      return FALSE;
    
    if (isset($response[$shelfId][$this->name]))
      return $response[$shelfId][$this->name];
      
    $model = new Shelf();
    
    return $response[$shelfId][$this->name] = (bool)$model->fetchRow($model->select()
                                                          ->where('id=?', $shelfId)
                                                          ->where('projectName=?', $this->name));
    
  }

}
