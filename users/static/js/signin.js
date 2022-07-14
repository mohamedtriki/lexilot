
document.getElementById('dashboard').addEventListener('click',function(){
  //   document.getElementById('signup_page').style.display="flex"
    document.getElementById('signup_cont').style.opacity=0
    document.getElementById('signup_page').style.display="flex"
    gsap.fromTo('#signup_cont',{opacity:0,scale:0.6},{opacity:1,scale:1})
    document.documentElement.style.overflow="hidden";
    $("html").getNiceScroll().hide();
  })

  document.getElementById('signup_page').addEventListener('click',function(){
    var lexilot= document.getElementById('lexilot');
    var isClickInsideElement = document.getElementById('signup_cont').contains(event.target);
    if (!isClickInsideElement) {
        document.getElementById('signup_page').style.display="none"
        document.documentElement.style.overflow="scroll";
        if (lexilot.style.display=="none"){
            $("html").getNiceScroll().show();
            
            
          }
    }
  })


document.getElementById('signin_title').addEventListener('click',function(){
    document.getElementById('signup_title').style.color='#BBBBBB'
    document.getElementById('signup_title').style.borderBottom= "0px solid #F9A0DE"
    document.getElementById('signin_title').style.color='#FFFFFF'
    document.getElementById('signin_title').style.borderBottom= "3px solid #F9A0DE"
    document.getElementById('logup').style.display='none'
    document.getElementById('login').style.display='block'


})
document.getElementById('signup_title').addEventListener('click',function(){
    document.getElementById('signin_title').style.color='#BBBBBB'
    document.getElementById('signin_title').style.borderBottom= "0px solid #F9A0DE"
    document.getElementById('signup_title').style.color='#FFFFFF'
    document.getElementById('signup_title').style.borderBottom= "3px solid #F9A0DE"
    document.getElementById('login').style.display='none'
    document.getElementById('logup').style.display='block'

})






// document.querySelectorAll('.buy').forEach(item => {
//   item.addEventListener('click', event => {
//     window.location.reload();

//   })
// })

const divs = document.querySelectorAll('.sign_button');

divs.forEach(el => el.addEventListener('click', event => {
  window.scrollTo(0, 0);
  document.getElementById('signup_cont').style.opacity=0
  document.getElementById('signup_page').style.display="flex"
  gsap.fromTo('#signup_cont',{opacity:0,scale:0.6},{opacity:1,scale:1})
  document.documentElement.style.overflow="hidden";
}));

// document.getElementById('buy1').addEventListener('click',function(){
//   document.getElementById('upgrade_wrapper2').style.display="flex"
//   gsap.fromTo('#signup_cont',{opacity:0,scale:0.6},{opacity:1,scale:1})
//   })
  







