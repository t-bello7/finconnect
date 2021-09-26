const hamburger = document.querySelector(".navbar__toggle")
const navul = document.querySelector(".nav");
const loader = document.querySelector(".loader");

console.log(navul)
function toggleNav(){
    console.log('hey');
    navul.classList.toggle('show');
    console.log(navul)
}
hamburger.addEventListener('click', toggleNav);

// $.ajax({
//     type:'GET',
//     url:'/',
//     success: function(res){
//         setTimeout(()=>{
//             spinner.classList.add('no-show')
//             console.log('{{listings}}')
//         }, 500)

//     },
//     error: function(er){
//         console.log("error");
//     }
// })

// $(window).on('load',function(){
//     $(".loader-wrapper").fadeOut("slow");
// })

// add onload = myFunction in the body 
// function myFunction(){
//     spinner.style.display = 'none';
// }


window.addEventListener("load", function(){
    loader.classList.add('hidden');
});