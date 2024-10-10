questions = []
cleaned_list=[]
evaluated_list=[] 
answers_list = []

## while loop seperates the list and appends only the questions
def get_questions_list(text):
    counter =0 
    while counter < (len(text)):
        t = text[counter]
        questions.append(t[1])
        counter+=1
    return questions

### removes the "=" so that eval can be used 
def get_cleaned_list(questions):
    counter = 0 
    while counter < (len(questions)):
        t = questions[counter]
        q=t.split("=")
        cleaned_list.append(q[0])
        counter+=1
    return cleaned_list

def get_answers_list(questions):  ### doesn't read handwriting for some reason ##
    counter = 0 
    temp_list =[]
    while counter < (len(questions)):
        t = questions[counter]
        q=t.split("=")
        temp_list.append(q[1])
        answers_list = [eval(add) for add in temp_list]
        counter+=1
    return answers_list

def get_evaluated_list(cleaned_list):
    evaluated_list = [eval(add) for add in cleaned_list]
    return evaluated_list