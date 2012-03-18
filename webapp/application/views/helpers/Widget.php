<?php

class Appdate_View_Helper_Widget extends Zend_View_Helper_Abstract {

  public function widget($name, $args=null) {
    $output = $this->{$name}($args);
    return $output;
  }

  private function shelf() {
    $shelfId = Zend_Registry::get('shelfId');
    
    $output = "<h3>Your shelf <a class='small' title='Learn more about the shelf' href='/page/shelf'>?</a></h3>";

    if (empty($shelfId)) {
      $output .=<<<EOHTML
      <form id="frmShelfCreate" method="post" action="/shelves/open">
        <p class="formRow" id="lbl1">You've not opened a shelf, yet.</p>
        <p class="formRow hide" id="lbl2">Enter you shelf id:</p>
        <p class="formRow center" id="enterId">(<span class="actuator hide-lbl1 show-lbl2 hide-enterId show-shelfIdRow show-cancel">I already have a shelf id</span>)</p>
        <div class="formRow hide" id="shelfIdRow">
          <input type="text" name="shelfId">
        </div>
        <div class="formRow">
          <input type="submit" value="Open!">
          <span id="cancel" class="hide">or <a href="/">Cancel</a></span>
        </div>
      </form>
EOHTML;
      return $output;
    }
    
    # Load the shelf for this shelfId
    $model = new Shelf();
    
    $projects = $model->fetchAll($model->select()->where('id=?', $shelfId));
    
    if (count($projects) > 0) {
      $output .= '<ul>';
      foreach($projects as $project) {
        $output .= "<li>{$project->projectName}</li>";
      }
      $output .= '</ul>';

      $output .="<p><a href='/shelf/{$shelfId}'>View the full project list</a></p>";
      $output .="<p><a href='/shelf/{$shelfId}?format=xml'>Grab your shelf RSS</a></p>";
    } else {
      $output .= "<p>Add/Remove projects to the shelf by (un)checking the box near their name.</p>"; 
    }
    
      $output .="<p>Your shelf ID is: <span class='quiet'>{$shelfId}</span></p>";
      $output .=<<<EOHTML
      <form id="frmShelfCreate" method="post" action="/shelves/purge">
        <div class="formRow">
          <input type="submit" class="confirm" title="All projects (if any) will be removed and the shelf discarded.\nYour current RSS will not work anymore." value="Discard shelf">
        </div>
      </form>
EOHTML;
    
    return $output;
  }

  private function twitterFollow() {

    return <<< EOHTML
    <div style="text-align: center">
    <p>Get updates via Twitter!</p>
    <p>
<a href="https://twitter.com/Appdateit" class="twitter-follow-button" data-show-count="false" data-size="large">Follow @Appdateit</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</p>
</div>
EOHTML;

  }

  private function searchForm() {
    return <<< EOHTML
      <form id="frmSearch" action="/search">
      <div>
        <input type="text" class="text" name="q" value="{$this->view->escape($this->view->q)}">
        <input type="submit" class="button" value="Search">
      </div>
      </form>
EOHTML;
  }
  
  private function getSatisfaction($args) {
    if ('development' == APPLICATION_ENVIRONMENT)
      return;
    
    if ($args['module'] == 'css') {
      return <<< EOHTML
<style type='text/css'>@import url('http://s3.amazonaws.com/getsatisfaction.com/feedback/feedback.css');</style>
EOHTML;
    }
    
    if ($args['module'] == 'js') {
      return <<< EOHTML
<script src='http://s3.amazonaws.com/getsatisfaction.com/feedback/feedback.js' type='text/javascript'></script>
<script type="text/javascript" charset="utf-8">
  var tab_options = {}
  tab_options.placement = "left";  // left, right, bottom, hidden
  tab_options.color = "#222"; // hex (#FF0000) or color (red)
  GSFN.feedback('http://getsatisfaction.com/appdate/feedback/topics/new?display=overlay&style=idea', tab_options);
</script>
EOHTML;
    }
  }
  

}
