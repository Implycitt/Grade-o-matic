from PIL import Image
import pytesseract

# pt is not working for some reason if the path is not explicitly stated so im keeping it here (DO NOT TOUCH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = r'..\input\math.jpg'

def read_image(path: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
