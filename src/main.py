from PIL import Image
import pytesseract
questions = []

# Path to the image
image_path = r'..\Grade-o-matic-1\input\math.png'

# Open the image using PIL
image = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)
print(text)## TESTING PURPOSES## 