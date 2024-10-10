from PIL import Image
import easyocr as es

questions = []
cleaned_list=[]
evaluated_list=[]

reader = es.Reader(['en'])


image_path = r'..\input\handwriting_2_.jpg'
image = Image.open(image_path)

text = reader.readtext(image_path)

## TESTING PURPOSES##
counter = 0 
while counter < (len(text)):
    t = text[counter]
    questions.append(t[1])
    counter+=1
print(questions)