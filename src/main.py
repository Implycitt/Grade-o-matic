from PIL import Image
import pytesseract
questions = []
cleaned_list=[]
evaluated_list=[]

# pt is not working for some reason if the path is not explicitly stated so im keeping it here (DO NOT TOUCH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image
image_path = r'..\input\math.jpg'

# Open the image using PIL
image = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# cleans the data and gets a clean list from the text
questions.append(text.split("="))
cleaned_list = [q.strip() for question in questions for q in question]
evaluated_list = [eval(add) for add in cleaned_list]


## TESTING PURPOSES## 
print(text)
print(cleaned_list)
print(evaluated_list)
