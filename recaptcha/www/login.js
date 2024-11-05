//document.getElementById('login_form').addEventListener('submit', function (event) {
//    event.preventDefault();
//
//    // Get the reCAPTCHA response token
//    const recaptchaResponse = grecaptcha.getResponse();
//
//    // Check if reCAPTCHA is verified
//    if (recaptchaResponse.length === 0) {
//        alert('Please verify that you are not a robot.');
//        return false;
//    }
//
//    // Prepare form data
//    const formData = new FormData();
//    formData.append('token', recaptchaResponse);
//    formData.append('username', document.getElementById('username').value);
//    formData.append('password', document.getElementById('password').value);
//
//    // Send the data to the backend using fetch
//    fetch('/api/method/recaptcha.www.login_validation.verify_recaptcha', {
//        method: 'POST',
//        body: formData
//    })
//    .then(response => {
//        if (!response.ok) {
//            throw new Error('Network response was not ok');
//        }
//        return response.json();
//    })
//    .then(data => {
//        console.log('API response:', data); // Debugging: log the response
//        if (data.message === true) {
//            window.location.href = '/app/home'; // Redirect to home if login is successful
//        } else {
//            alert(data.error || 'Invalid login credentials. Please try again.');
//        }
//    })
//    .catch(error => {
//        console.error('Error:', error);
//        alert('An error occurred during login. Please try again later.');
//    });
//});


//document.getElementById('login_form').addEventListener('submit', function (event) {
//    // Prevent default form submission
//    event.preventDefault();
//
//    // Get the reCAPTCHA response token
//    const recaptchaResponse = grecaptcha.getResponse();
//
//    // Check if reCAPTCHA is verified
//    if (recaptchaResponse.length === 0) {
//        alert('Please verify that you are not a robot.');
//        return false;
//    }
//
//    // Set the token input value with the reCAPTCHA token
//    document.getElementById('recaptcha_token').value = recaptchaResponse;
//
//    // Submit the form
//    this.submit();
//});


