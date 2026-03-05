import easyocr

reader = easyocr.Reader(['en'])

def detect_vehicle_number(frame):

    results = reader.readtext(frame)

    for (bbox, text, prob) in results:

        if prob > 0.5:
            return text

    return None