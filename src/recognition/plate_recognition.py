import easyocr

reader = easyocr.Reader(['en'])

def read_plate(plate_img):
    result = reader.readtext(plate_img)
    if result:
        return result[0][1]
    return None