from flask import Flask, request, send_file, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')

    # Encode the prompt for URL
    encoded_prompt = requests.utils.quote(prompt)

    # Create the URL
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    # Get the image
    response = requests.get(url)

    # Save the image
    filename = "generated_image.png"
    with open(filename, "wb") as f:
        f.write(response.content)

    return jsonify({"message": "Image generated successfully"})


@app.route('/get_image')
def get_image():
    return send_file('generated_image.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)