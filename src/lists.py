equation = []
question=[]
evaluated_list=[] 
answers_list = []

## while loop seperates the text list and appends only the equations 
def get_equation_list(text):
    counter = 0 
    while counter < (len(text)):
        t = text[counter]
        equation.append(t[1])
        counter+=1
    return equation

### splits the "=" from the equation list so we get only the questions 
def get_cleaned_list(equation):
    counter = 0 
    while counter < (len(equation)):
        t = equation[counter]
        q=t.split("=")   
        if "x" in q[0].lower(): ### replaces "x" with "*"
            q[0]=q[0].replace("x","*")
            q[0]=q[0].replace("X","*")
        for char in q[0]:
            if char.isalpha():
                q[0]='0'
        else:
            question.append(q[0])
        counter+=1
    return question

def get_answers_list(equation): ### Gets answers from the equations list 
    temp_list =[]
    for t in equation:
        q = t.split("=")
        if len(q)<2:
            q.append("")
        answer =q[1]
        if answer.replace('.', '', 1).isdigit(): ## checks if the question was left blank or if the answer is a number
            temp_list.append(answer)
        else:
            temp_list.append('0') 
        answers_list = [eval(add) for add in temp_list]
    return answers_list

def get_evaluated_list(question):
    evaluated_list = [eval(add) for add in question]
    return evaluated_list