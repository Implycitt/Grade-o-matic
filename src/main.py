import vision, formulas

multPath = r'..\input\multiplication.jpg'
mathPath = r'..\input\math.jpg'

def main():
    equations = vision.imgRead(mathPath)
    equation, answer = equations[0]
    test = formulas.formula(equation, answer)
    print(test.getEquation())

if __name__ == "__main__":
    main()

