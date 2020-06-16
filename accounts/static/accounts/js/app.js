$("input").focus(function() {
  $(this).css("background-color","#9999ff");
});

$("input").blur(function() {
  $(this).css("background-color","white");
});

$("#close").click(function() {
  $("#messages").fadeOut(500);
})
