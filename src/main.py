import vision, formulas

multPath = r'..\input\handwriting2.jpg'
mathPath = r'..\input\math.jpg'

def main():
    right, total = 0, 0
    equations = vision.imgRead(multPath)
    for i in equations:
        equation, answer = i
        test = formulas.formula(equation, answer)
        right += test.check()
        total += 1
    print(f'{right}/{total}')

if __name__ == "__main__":
    main()

