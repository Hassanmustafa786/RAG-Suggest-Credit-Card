// static/script.js
function sendRequest() {
    const message = document.getElementById('message').value;
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message': message
        })
    })
    .then(response => response.json())
    .then(data => {
        // Extract the response from the data object
        var responseText = data.response;
        // Display the response in the HTML element with id 'response'
        document.getElementById('response').innerText = responseText;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
