$(function() {

  $('h4 input[type=checkbox]').click(function() {
      var w = $("#shelf .loading").show();
      var el = $(this);
      $.post('/shelves/toggle', 
         {format: 'json', projectName: $(this).attr('title')},
         function(r,s) {
           if (s == 'success') {
             w.hide();
             el.parents('ul:first').toggleClass('inShelf');
             // Refresh the Shelf box
             $('#shelf .content').load('/shelves/box');
           }
         }
        );
  });

  $('.actuator').live('click', function() {
      var shows = this.className.match(/show-\w+/g);
      for (var i=0; i < shows.length; i++) {
        $('#'+shows[i].replace('show-','')).show();
      }
      var hides = this.className.match(/hide-\w+/g);
      for (var i=0; i < hides.length; i++) {
        $('#'+hides[i].replace('hide-','')).hide();
      }
      if ($(this).hasClass('autohide')) {
        $(this).hide();
      }
      
  });
  
  $('.confirm').live('click', function() {
    return confirm($(this).attr('title') + " Confirm?");
  })
  

});
