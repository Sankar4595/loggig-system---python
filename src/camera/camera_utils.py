import cv2

def draw_label(frame, text, x, y):
    cv2.rectangle(frame, (x, y - 20), (x + 180, y), (0, 255, 0), -1)
    cv2.putText(frame, text, (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)