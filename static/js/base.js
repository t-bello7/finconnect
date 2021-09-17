const hambuger = document.querySelector(".nav")
const navul = document.querySelector('nav');

function toggleNav(){
    navul.classList.toggle('show');
}


hamburger.addEventListner('click',toggleNav);