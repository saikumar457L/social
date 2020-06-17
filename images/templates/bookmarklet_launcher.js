(function () {
  if (window.myBookmarklet !== undefined) {
    myBookmarklet();
  }
  else {
    document.body.appendChild(document.createElement('script')).src='https://powerful-mountain-27271.herokuapp.com/static/images/js/bookmarklet.js?r='+Math.floor(Math.random()*999999);
  }
})();
