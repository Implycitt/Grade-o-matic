from PIL import Image
import pytesseract
questions = []
cleaned_list=[]

# Path to the image
image_path = r'..\Grade-o-matic-1\input\math.jpg'

# Open the image using PIL
image = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

questions.append(text.split("="))
for question in questions:
    for q in question:
        cleaned_list.append(q.strip())


## TESTING PURPOSES## 
print(text)
print(cleaned_list)
