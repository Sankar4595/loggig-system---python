from flask import Flask, request, jsonify
import cv2
import numpy as np
import easyocr
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize OCR reader
reader = easyocr.Reader(['en'])

def extract_vehicle_number(text_list):

    pattern = r'[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{3,4}'

    for text in text_list:
        cleaned = re.sub(r'[^A-Z0-9]', '', text.upper())

        match = re.search(pattern, cleaned)

        if match:
            return match.group()

    return None

@app.route('/scan-vehicle', methods=['POST'])
def scan_vehicle():

    print("Request received")

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']

    img_bytes = file.read()
    npimg = np.frombuffer(img_bytes, np.uint8)

    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"error": "Invalid image"}), 400

    print("Image received")

    # Run OCR
    results = reader.readtext(frame)

    detected_texts = []

    for (bbox, text, prob) in results:
        print("Detected:", text, prob)
        detected_texts.append(text)

    vehicle_number = extract_vehicle_number(detected_texts)

    return jsonify({
        "vehicle_number": vehicle_number
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)