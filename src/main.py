import vision

questions = []
cleaned_list=[]
evaluated_list=[]


image_path = r'..\input\math.jpg'
text = vision.read_image(image_path)

# cleans the data and gets a clean list from the text
questions.append(text.split("="))
cleaned_list = [q.strip() for question in questions for q in question]
evaluated_list = [eval(add) for add in cleaned_list]

## TESTING PURPOSES## 
print(text)
print(cleaned_list)
print(evaluated_list)
