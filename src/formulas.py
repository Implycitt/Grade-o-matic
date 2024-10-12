import lists 


class equations:
    equation: str
    answer: int
    def __init__(self,equation):
        self.equation = equation
    
    def to_dict(self):
        if "x" in self.equation:
            return {self.equation: "multiplication"}
        if "+" in self.equation:
            return {self.equation: "addition"}
        if "-" in self.equation:
            return {self.equation: "subtraction"}
        
    def __str__(self):
        return f"Equation: {self.equation}"