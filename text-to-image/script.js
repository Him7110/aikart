// script.js
async function generateImage() {
    const text = document.getElementById('textInput').value.trim();
    if (!text) {
        alert('Please enter some text.');
        return;
    }

    const response = await fetch('/generate-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });

    const imageData = await response.blob();
    const imageUrl = URL.createObjectURL(imageData);
    document.getElementById('imageContainer').innerHTML = `<img src="${imageUrl}" alt="Generated Image">`;
}
