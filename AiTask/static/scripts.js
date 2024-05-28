document.getElementById('send-button').addEventListener('click', function() {
    var userInput = document.getElementById('user-input');
    var chatBox = document.getElementById('chat-box');

    var message = userInput.value;
    if (message.trim() === '') return;

    // Add user message to chat box
    var userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = message;
    chatBox.appendChild(userMessage);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;

    // Disable input and button
    userInput.disabled = true;
    document.getElementById('send-button').disabled = true;

    // Show loading indicator
    var loadingIndicator = document.createElement('div');
    loadingIndicator.id = 'loading';
    loadingIndicator.textContent = 'Processing...';
    chatBox.appendChild(loadingIndicator);

    // Fetch response from the backend
    fetch('/Chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            base_url: "http://localhost/wordpress",
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        // Remove loading indicator
        chatBox.removeChild(loadingIndicator);

        // Format response
        var formattedResponse = formatResponse(data.response);

        // Add bot message to chat box
        var botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.innerHTML = formattedResponse;
        chatBox.appendChild(botMessage);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;

        // Re-enable input and button
        userInput.disabled = false;
        document.getElementById('send-button').disabled = false;

        // Clear user input
        userInput.value = '';
        userInput.focus();
    });
});

function formatResponse(response) {
    return response
        .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>') // Make text bold
        .replace(/\* (.*?)(\n|$)/g, '<br>• $1<br>'); // Add new line and bullet
}
