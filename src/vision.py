from PIL import Image
import pytesseract
import easyocr as es

# pt is not working for some reason if the path is not explicitly stated so im keeping it here (DO NOT TOUCH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = r'..\input\math.jpg'

def imgRead(path: str) -> list: 
    reader = es.Reader(['en'])
    data = reader.readtext(path)
    ret = []
    for i in data:
        ret.append(getParts(i))
    return ret

def getParts(data: list) -> tuple:
    try:
        equation, answer = data[1].split('=')
    except:
        equation, answer = data[1][:-1], ''
    equation = clean(equation)
    return (equation, answer)

def clean(equation: list) -> list:
    cleaned, nums = [], [] 
    for part in equation:
        if part == ' ' or part == '=': continue
        if not str.isdigit(part):
            cleaned.append(nums)
            nums = []
            cleaned.append(part)
            continue
        nums.append(part)
    cleaned.append(nums)
    cleaned = [''.join(i) for i in cleaned]
    return cleaned
