const name = document.getElementById('name');
const nationality = document.getElementById('nationality');
const phone = document.getElementById('phone');
const email = document.getElementById('email');
const dateOfTravel = document.getElementById('dateOfTravel');
const cityOfResidence = document.getElementById('cityOfResidence');
const noOfPassengers = document.getElementById('noOfPassengers');
const checkDefault = document.getElementById('checkDefault');
const submit = document.getElementById('submit');

const nameError = document.getElementById('nameError');
const nationalityError = document.getElementById('nationalityError');
const phoneError = document.getElementById('phoneError');
const emailError = document.getElementById('emailError');
const dateError = document.getElementById('dateError');
const cityError = document.getElementById('cityError');
const passengersError = document.getElementById('passengersError');
const checkError = document.getElementById('checkError');

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

submit.addEventListener('click', function() {
    let isValid = true;

    if (name.value.trim() === '') {
        nameError.textContent = 'Name is required.';
        isValid = false;
    } else {
        nameError.textContent = '';
    }

    if (nationality.value.trim() === '') {
        nationalityError.textContent = 'Nationality is required.';
        isValid = false;
    } else {
        nationalityError.textContent = '';
    }

    if (phone.value.trim() === '') {
        phoneError.textContent = 'Phone number is required.';
        isValid = false;
    } else {
        phoneError.textContent = '';
    }

    if (email.value.trim() === '') {
        emailError.textContent = 'Email is required.';
        isValid = false;
    } else if (!validateEmail(email.value.trim())) {
        emailError.textContent = 'Invalid email format.';
        isValid = false;
    } else {
        emailError.textContent = '';
    }

    if (dateOfTravel.value.trim() === '') {
        dateError.textContent = 'Date of travel is required.';
        isValid = false;
    } else {
        dateError.textContent = '';
    }


    if (cityOfResidence.value.trim() === '') {
        cityError.textContent = 'City of residence is required.';
        isValid = false;
    } else {
        cityError.textContent = '';
    }


    if (!checkDefault.checked) {
        checkError.textContent = 'You must agree to the terms and conditions.';
        isValid = false;
    } else {
        checkError.textContent = '';
    }

    if (isValid) {
        alert('Form submitted successfully!');
    }
});
