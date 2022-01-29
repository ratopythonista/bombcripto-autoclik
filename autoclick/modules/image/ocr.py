import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def image_to_float(image):
    image_text = pytesseract.image_to_string(image)
    return float(image_text.replace(",", "."))


def image_to_text(image):
    image_text = pytesseract.image_to_string(image)
    return image_text