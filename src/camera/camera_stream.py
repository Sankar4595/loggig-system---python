import cv2

def get_camera(camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        raise Exception("Camera not accessible")
    return cap