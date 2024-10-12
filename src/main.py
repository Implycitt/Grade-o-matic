import vision
import lists ### refer to lists file##
import Grader

image_path = r'..\input\multiplication.jpg'

text = vision.EasyOCR(image_path) ### reads the image and gets a big list#

equation = lists.get_equation_list(text)
questions = lists.get_cleaned_list(equation)
evaluated_list = lists.get_evaluated_list(questions)
answers = lists.get_answers_list(equation)
Grade = Grader.Grade(evaluated_list, answers)

print(f"Equation \n{equation}")
print(f"Question \n{questions}")
print(f"evaluated list \n{evaluated_list}")
print(f"answers list \n{answers}")
print(f"Grade: {Grade}%")