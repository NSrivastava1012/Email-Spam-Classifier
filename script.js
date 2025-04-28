// script.js

// Optional: Disable button on submit to show feedback
document.getElementById('spamForm').addEventListener('submit', function() {
    const button = document.querySelector('button');
    button.innerText = "Checking...";
    button.disabled = true;
});
