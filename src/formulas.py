class formula:
    equation: list 
    answer: int

    def __init__(self, equation, answer):
        self.equation = equation
        self.answer = answer

    def getAnswer(self):
        return self.answer

    def getEquation(self):
        return self.equation
