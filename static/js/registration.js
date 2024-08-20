function toggleFields() {
    const customerFields = document.querySelectorAll('.customer-field');
    const companyFields = document.querySelectorAll('.company-field');
    const isCustomer = document.getElementById('customer').checked;

    customerFields.forEach(field => {
        field.style.display = isCustomer || !isCustomer ? 'block' : 'none';
    });
    companyFields.forEach(field => {
        field.style.display = !isCustomer ? 'flex' : 'none';
    });
}
function submitForm(event) {
    event.preventDefault();
    const formData = {
        companyName: document.getElementById('companyName').value,
        companyTelephone: document.getElementById('companyTelephone').value,
        firstName: document.getElementById('firstName').value,
        middleName: document.getElementById('middleName').value,
        lastName: document.getElementById('lastName').value,
        mobileNumber: document.getElementById('mobileNumber').value,
        emailId: document.getElementById('emailId').value,
        password: document.getElementById('password').value,
        state: document.getElementById('state').value,
        city: document.getElementById('city').value,
        street1: document.getElementById('street1').value,
        street2: document.getElementById('street2').value,
        pinCode: document.getElementById('pinCode').value,
        sex: document.getElementById('sex').value,
        age: document.getElementById('age').value,
        dob: document.getElementById('dob').value
    };

    fetch('/registration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect_url) {
            window.location.href = data.redirect_url;
            console.log(window.location.href);
        } else {
            console.error('Error:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
