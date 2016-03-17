var char2Right = -0.1;
var charLeft = -0.06;
function resizeInterface(){
  appWidth = $("body").width();
  $("#fixed-chara").css({'width':appWidth * 0.6,'left':appWidth * -0.06,'bottom':appWidth * -0.16});
  $("#fixed-chara2").css({'width':appWidth * 0.35,'right':appWidth * char2Right,'top':appWidth * 0.05});
  $("form").css({'width':appWidth * 0.7 - 100,'margin-left':'15%'});
  $(".default-text").css({'width':appWidth * 0.7 - 140});
  $(".default-textarea").css({'width':appWidth * 0.7 - 140});
  $("button").css({'width':appWidth * 0.7 - 140});
  $("#fixed-chara2").show();
  if($(window).width() < 600){
    $("form").css({'width':appWidth - 90,'margin-left':0});
    $("#fixed-chara2").hide();
  }
}

$(function(){
  resizeInterface();
  runEnterAnimation();
  $(window).scroll(function(){
    if($(window).scrollTop() > 75){
      char2Right = -0.2;
      charLeft = -0.1;
      TweenLite.to($("h1"),0.3,{'font-size':'20px','height':"50px",'line-height':"50px"});
    } else {
      char2Right = -0.1;
      charLeft = -0.06;
      TweenLite.to($("h1"),0.3,{'font-size':'40px','height':"120px",'line-height':"120px"});
    }
    TweenLite.to($("#fixed-chara2"),0.7,{'right':appWidth * char2Right});
    TweenLite.to($("#fixed-chara"),0.7,{'left':appWidth * charLeft});
  });
});
