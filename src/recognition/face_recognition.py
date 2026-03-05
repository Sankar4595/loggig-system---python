import cv2
import os
import json
import numpy as np

# Load employee data
with open("models/employees.json", "r") as f:
    EMPLOYEES = json.load(f)

model = cv2.face.LBPHFaceRecognizer_create()
DATASET_PATH = "models/faces"

faces = []
ids = []
labels = {}
label_id = 0

# Train model from static images
for file in os.listdir(DATASET_PATH):
    if file.endswith(".jpg"):
        emp_id = file.split("_")[0]

        img = cv2.imread(os.path.join(DATASET_PATH, file), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (200, 200))

        if emp_id not in labels:
            labels[emp_id] = label_id
            label_id += 1

        faces.append(img)
        ids.append(labels[emp_id])

model.train(faces, np.array(ids))
reverse_labels = {v: k for k, v in labels.items()}

def recognize_face(face_img):
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (200, 200))

    label, confidence = model.predict(gray)

    if confidence < 70:
        emp_id = reverse_labels.get(label)
        return EMPLOYEES.get(emp_id)

    return None