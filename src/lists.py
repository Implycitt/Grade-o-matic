questions = []
cleaned_list=[]
evaluated_list=[] 

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


def get_evaluated_list(cleaned_list):
    for add in cleaned_list:
        evaluated_list.append(eval(add))
    return evaluated_list