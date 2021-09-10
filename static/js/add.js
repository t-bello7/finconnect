// const satAvailableField = document.querySelector('#satAvailableField')
// const satWorkHours = document.querySelector('.sat_work_hours')


// let checkBoxClick = 0;
// satAvailableField.addEventListener('click', (e)=>{
//     checkBoxClick += 1
//     const satAvailableVal = e.target.value;
//     // console.log(satAvailableVal)
//     console.log(typeof(satAvailableVal));
//     if (satAvailableVal === 'on' && checkBoxClick % 2 === 1){
//         satWorkHours.style.display = "block";
//         fetch('/listing/add-institution', {
//         body:JSON.stringify({checkbox:checkBoxClick}),
//         method: "POST"})
//     } else{
//         satWorkHours.style.display = "none";
//     }
// })