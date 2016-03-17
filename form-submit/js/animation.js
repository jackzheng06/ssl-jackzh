function runEnterAnimation(){
  //Execute enter animation
  TweenLite.from($("#fixed-chara"),1,{'left':'-100%'});
  TweenLite.from($("#fixed-chara2"),1,{'top':'-100%'});
  TweenLite.from($("h1"),1,{'top':'-200px'});
}
