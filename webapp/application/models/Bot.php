<?php

Class Bot {

  public function fetchAll() {
    
    $cfg = Zend_Registry::get('configuration');

    $bots = array();
    
    if (!file_exists($cfg->bots->directory))
      return $bots;
    
    foreach(glob($cfg->bots->directory . '/B*.py') as $file) {
      $pi = pathinfo($file);
      $bot['path'] = $pi['dirname'];
      $bot['filename'] = $pi['basename'];
      $bot['basename'] = $pi['filename'];
      $bot['size'] = filesize($file);
      $bots[] = (object)$bot;
    }

    return $bots; 
    
  }

  public function fetch($name) {
    
    $cfg = Zend_Registry::get('configuration');
    
    if (!file_exists($cfg->bots->directory))
      return 'Error reading bot directory';
    
    if (!file_exists($cfg->bots->directory . "/{$name}.py"))
      return 'Error reading bot file';
    
    return file_get_contents($cfg->bots->directory . "/{$name}.py");
    
  }
  
}


