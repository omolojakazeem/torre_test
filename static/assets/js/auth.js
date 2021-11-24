$(".login").hide();
$(".register_li").addClass("active");

$(".login_li").click(function(){
  $(this).addClass("active");
  $(".register_li").removeClass("active");
  $(".login").show();
   $(".register").hide();
})

$(".register_li").click(function(){
  $(this).addClass("active");
  $(".login_li").removeClass("active");
  $(".register").show();
   $(".login").hide();
})