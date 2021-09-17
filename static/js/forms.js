
import NaijaStates  from 'naija-state-local-government';


const emailField = document.querySelector('#emailField');
const feedBackField = document.querySelector('.invalid_feedback');
const successOutput = document.querySelector('.success_feedback');
const showPasswordToggle = document.querySelector('.showPasswordToggle')
const passwordFieldToggle = document.querySelector('#passwordField');
const submitBtn = document.querySelector('.submit-btn')
// const satAvailableField = document.querySelector('#satAvailableField')
const satWorkHours = document.querySelector('.sat_work_hours')


console.log(NaijaStates.all());

emailField.addEventListener('keyup', (e)=>{
    const emailVal = e.target.value;
    successOutput.style.display="block";

    successOutput.textContent = `Checking ${emailVal}`;
    emailField.classList.remove('.is-error');
    feedBackField.style.display = 'none';
    if (emailVal.length > 0 ){    
        fetch('/auth/validate-email', {
        body:JSON.stringify({email:emailVal}),
        method: "POST",
    }).then(res=>res.json())
    .then((data)=>{
        console.log('data', data);
        successOutput.style.display="none";
        if(data.email_error){
            submitBtn.disabled = true;
            emailField.classList.add('.is-error')
            feedBackField.style.display = 'block'
            feedBackField.innerHTML = `<p>${data.email_error}<p>`
        }else{
            submitBtn.removeAttribute('disabled');
        }
    });

}
});

const handleToggleInput = (e) =>{
    if(showPasswordToggle.textContent === 'SHOW'){
        passwordFieldToggle.setAttribute("type", "text");
        showPasswordToggle.textContent = "HIDE";
    }else{
        showPasswordToggle.textContent = "SHOW";
        passwordFieldToggle.setAttribute("type", "password");
    }
}

showPasswordToggle.addEventListener('click', handleToggleInput);


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