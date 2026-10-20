(function(){
  document.documentElement.classList.add('js');
  function init(){
    var els=document.querySelectorAll('.vr .reveal');
    if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return}
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.12});
    els.forEach(function(e){io.observe(e)});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
