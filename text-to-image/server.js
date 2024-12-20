// server.js
const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('isomorphic-fetch');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

// Stability AI API endpoint
const API_ENDPOINT = 'https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image';
// Your Stability AI API key
const API_KEY = "sk-aiy0JA12L82qobuIcnWjW1qMxxTEuL7OoPqPGGvXQ6HbRWIY";

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/generate-image', async (req, res) => {
    const { text } = req.body;

    if (!text) {
        return res.status(400).json({ error: 'Text field is required' });
    }

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`
    };

    const payload = {
        text_prompts: [{ text }],
        cfg_scale: 7,
        height: 1024,
        width: 1024,
        samples: 1,
        steps: 30
    };

    try {
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            headers,
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error('Failed to generate image');
        }

        const imageBuffer = await response.buffer();
        fs.writeFileSync('./public/generated-image.png', imageBuffer);

        res.status(200).json({ message: 'Image generated successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to generate image' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
