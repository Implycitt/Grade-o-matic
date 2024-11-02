def Grade(evaluated_list, answers_list):
    equal_count = sum(1 for a, e in zip(answers_list, evaluated_list) if a == e) ## checks how many times answer and evaluated are the same
    total = len(evaluated_list)
    return (equal_count/total)*100