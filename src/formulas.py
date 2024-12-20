class formula:
    equation: list 
    givenAnswer: int
    actualAnswer: int | None

    def __init__(self, equation, answer):
        self.equation = equation
        self.givenAnswer = answer
        self.actualAnswer = None 

    def getGiven(self):
        return self.givenAnswer

    def getActual(self):
        if self.actualAnswer is None:
            return self.solve()
        return self.actualAnswer

    def getEquation(self):
        return self.equation

    def solve(self):
        return eval(''.join(self.equation))

    def check(self):
        if self.actualAnswer is None:
            self.actualAnswer = self.getActual()
        return (int(self.actualAnswer) == int(self.givenAnswer))


