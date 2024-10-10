import pytesseract
from PIL import Image
image_path = '../input/math.png'

def read(image_path: str) -> list:
    image = Image.open(image_path)
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)

words = read(image_path)
print(words)
