from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import pytesseract

app = Flask(__name__)
CORS(app)

# Tesseract config
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

@app.route('/scan-vehicle', methods=['POST'])
def scan_vehicle():

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']

    img_bytes = file.read()
    npimg = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Image preprocessing
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)

    # OCR
    text = pytesseract.image_to_string(gray, config='--psm 8')

    vehicle_number = text.strip()

    if vehicle_number == "":
        return jsonify({"vehicle_number": None})

    return jsonify({
        "vehicle_number": vehicle_number
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)