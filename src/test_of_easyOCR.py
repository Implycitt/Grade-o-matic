from PIL import Image
import easyocr as es

questions = []
cleaned_list=[]
evaluated_list=[]

reader = es.Reader(['en'])


image_path = r'..\input\math.jpg'
image = Image.open(image_path)

text = reader.readtext(image_path) ### reads the image and gets a big list#

## TESTING PURPOSES##
counter = 0 

## while loop seperates the list and appends only the questions
while counter < (len(text)):
    t = text[counter]
    questions.append(t[1])
    counter+=1

### removes the "=" so that eval can be used 
counter = 0 
while counter < (len(questions)):
    t = questions[counter]
    q=t.split("=")
    cleaned_list.append(q[0])
    counter+=1
print(cleaned_list)

## evals and adds to the evaluated list 
for add in cleaned_list:
    evaluated_list.append(eval(add))
print(evaluated_list)