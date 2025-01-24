from flask import Flask, request, send_file, jsonify
import requests
import os
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

CELEBRITIES = [
    "Taylor Swift", "Dwayne Johnson", "Beyoncé", "Leonardo DiCaprio",
    "Ariana Grande", "Chris Hemsworth", "Scarlett Johansson", "Tom Cruise",
    "Jennifer Lawrence", "Will Smith", "Angelina Jolie", "Brad Pitt",
    "Rihanna", "Lady Gaga", "Johnny Depp", "Emma Watson",
    "Robert Downey Jr.", "Chris Evans", "Zendaya", "Keanu Reeves",
    "Selena Gomez", "Kanye West", "Kim Kardashian", "Justin Bieber",
    "Billie Eilish", "Tom Holland", "Margot Robbie", "Gal Gadot",
    "Jason Momoa", "Ryan Reynolds", "Hugh Jackman", "Natalie Portman",
    "Anne Hathaway", "Matt Damon", "Ben Affleck", "Meryl Streep",
    "Daniel Radcliffe", "Emma Stone", "Chris Pratt", "Priyanka Chopra"
]


@app.route('/generate', methods=['POST'])
def generate_image():
    celebrity = random.choice(CELEBRITIES)

    prompt = f"a realistic photo of {celebrity} and Barack Obama holding hands together, photorealistic"
    encoded_prompt = requests.utils.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    response = requests.get(url)

    filename = "generated_image.png"
    with open(filename, "wb") as f:
        f.write(response.content)

    caption = f"{celebrity} and Barack Obama spotted together!"
    return jsonify({
        "message": "Image generated successfully",
        "caption": caption
    })


@app.route('/get_image')
def get_image():
    return send_file('generated_image.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)