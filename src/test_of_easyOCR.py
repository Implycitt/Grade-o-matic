import vision
import lists ### refer to lists file##


image_path = r'..\input\math.jpg'

text = vision.EasyOCR(image_path) ### reads the image and gets a big list#

questions = lists.get_questions_list(text)
cleaned_list = lists.get_cleaned_list(questions)
evaluated_list = lists.get_evaluated_list(cleaned_list)


print("Questions \n",questions)
print("cleaned list \n",cleaned_list)
print("evaluated list \n",evaluated_list)