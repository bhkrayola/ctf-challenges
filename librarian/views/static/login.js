// This would be part of your client-side JavaScript code
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    var formData = new FormData(this);
    fetch('/form_handler', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Alert the message
        
        if(data.success) {
            // If login is successful, wait 3 seconds, then redirect
            setTimeout(function() {
                window.location.href = '/thelibrary';
            }, 10000);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
