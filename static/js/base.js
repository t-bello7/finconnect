const satAvailableField = document.querySelector('#satAvailableField')
const satWorkHours = document.querySelector('.sat_work_hours')
// satAvailableField.value = 'off'
// console.log(satAvailableField.value)
let checkBoxClick = 0;
satAvailableField.addEventListener('click', (e)=>{
    checkBoxClick += 1
    let satAvailableVal = e.target.value;
    // satAvailableField.value = 'on'

    console.log(satAvailableVal)
    console.log(typeof(satAvailableVal));
    if (satAvailableVal === 'on' && checkBoxClick % 2 === 1){
        satWorkHours.style.display = "block";
        fetch('/list/checkbox', {
        body:JSON.stringify({checkbox:checkBoxClick}),
        method: "POST",}).then(res=> res.json())
        .then((data)=>{
            console.log('data', data);
            if (data.check_invalid){
                satAvailableField = 'off';
            }
        })
    } else{
        satWorkHours.style.display = "none";
    }
})