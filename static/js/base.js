const hamburger = document.querySelector(".navbar__toggle")
const navul = document.querySelector('.nav');

function toggleNav(){
    console.log('hey');
    navul.classList.toggle('show');
    console.log(navul)
}


hamburger.addEventListener('click', toggleNav);