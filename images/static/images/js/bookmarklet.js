(function() {
  var site_url = "https://powerful-mountain-27271.herokuapp.com/";
  var static_url = site_url+"static/";
  var min_width = 100;
  var min_height = 100;

  function bookmarklet(msg) {
      // loading of css
      var css = jQuery("<link>")
      css.attr({
        rel: 'stylesheet',
        type: 'text/css',
        href: static_url+'images/css/bookmarklet.css?r='+Math.floor(Math.random()*666666)
      });
      jQuery("head").append(css);
      // loading of ccs is completed.

      // loading of html block

      box_html = "<div id='bookmarklet' class='bookmarklet'> <a href='#' id='close' class='close'>&times; </a> <h1>Select image for bookmarking: </h1> <div id='images' class='images'> </div> </div>";
      jQuery("body").append(box_html);

      // loading of html block is completed.

      // finding the images

      jQuery.each(jQuery('img[src$="jpg"]'),function(index,image) {
        if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height) {
          image_url = jQuery(image).attr('src');
          jQuery("#bookmarklet .images").append('<a href = "#"> <img src="'+image_url+'"/> </a>');
        }
      });

      // finding images is completed

      // redirecting selected image to our site

      jQuery("#bookmarklet .images a").click(function(e) {
        console.log("initiled");
        selected_image = jQuery(this).children('img').attr('src');
        jQuery("#bookmarklet").hide();
        window.open(site_url+'images/create/?url='+encodeURIComponent(selected_image)+'&title='+encodeURIComponent(jQuery('title').text()),'_blank');
        console.log("success");
      });

      // end of redirecting slected image url

  }; // end function of bookmarklet

  // checking for jQuery if loaded

  if (typeof window.jQuery != 'undefined') {
    bookmarklet();
  }
  else {
    // checking for conflicts

    var conflict = typeof window.$ != 'undefined';
    var script = document.createElement("script");
    script.src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
    document.head.appendChild(script);

    // sanitation check fo jQuery load
    var attempts = 15;

    (function() {

      if (typeof window.jQuery == 'undefined') {
        if (--attempts > 0) {
          window.setTimeout(arguments.callee,250)
        }
        else {
          alert("An error ocurred while loading jQuery")
        }
      }
      else {
        bookmarklet();
      }

    })();
  }

})();
