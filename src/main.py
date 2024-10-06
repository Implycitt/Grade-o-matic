from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
questions = []

# Path to the image
image_path = r'C:\\Users\\nihal\\Documents\\GitHub\\AutoGrader_\\input\\math.png'

# Open the image using PIL
image = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)
print(text)## TESTING PURPOSES## 