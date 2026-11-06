(function(){
  var split=document.querySelector('.ex-split'); if(!split) return;
  var tabs=[].slice.call(split.querySelectorAll('.ex-tab')), cards=[].slice.call(split.querySelectorAll('.ex-card'));
  split.classList.add('ex-js');
  var mq=window.matchMedia('(max-width: 900px)');
  function show(id, focus, scroll){
    var card=document.getElementById(id); if(!card||cards.indexOf(card)<0) return;
    cards.forEach(function(c){c.classList.toggle('ex-on',c===card)});
    tabs.forEach(function(t){var on=t.getAttribute('aria-controls')===id;t.setAttribute('aria-selected',on?'true':'false');
      if(on&&mq.matches&&t.scrollIntoView){t.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'})}});
    if(scroll&&mq.matches){var y=card.getBoundingClientRect().top+window.scrollY-150;if(window.scrollY>y+40||window.scrollY<y-400)window.scrollTo({top:y,behavior:'smooth'})}
    if(focus) card.focus({preventScroll:true});
  }
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(e){e.preventDefault();var id=t.getAttribute('aria-controls');show(id,false,true);
      try{history.replaceState(null,'','#'+id)}catch(_){}});
    t.addEventListener('keydown',function(e){var k=e.key,n=null;
      if(k==='ArrowDown'||k==='ArrowRight')n=tabs[(i+1)%tabs.length];
      if(k==='ArrowUp'||k==='ArrowLeft')n=tabs[(i-1+tabs.length)%tabs.length];
      if(n){e.preventDefault();n.focus();n.click()}});
  });
  var h=location.hash.slice(1); if(h) show(h,false,false);
  window.addEventListener('hashchange',function(){show(location.hash.slice(1),false,true)});
})();
