$(document).ready(function () {

  'use strict';
 
  var typed = new Typed('.citations', {
      strings: ["Informatic subject.", "Web development.", "Mobile Development", "Software Development.", "Design.", "UX/UI.", "Marketing.", "Programming advices"],
      typeSpeed: 80,
      backSpeed: 60,
      backDelay: 3000,
      loop: true
  });
  
  
 $.fn.toggleSelected = function(options) {
    var defaults = $.extend({
      classes: 'selected',
      itemSelector: this.children().children(),
    });
    
    return this.each(function() {
      var o = defaults;
      var sel = o.itemSelector;
      
      sel.click(function() {
        var self = $(this);
        self.addClass(o.classes);
        self.siblings().removeClass(o.classes);
      });
    });
  };
  
  $('[data-toggle="selected"]').toggleSelected();
  
  new WOW().init();

});