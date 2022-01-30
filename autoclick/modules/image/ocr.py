import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def image_to_float(image):
    image_text = pytesseract.image_to_string(image)
    try:
        return float(image_text.replace(",", "."))
    except ValueError:
        return -1

def image_to_text(image):
    image_text = pytesseract.image_to_string(image)
    return image_text