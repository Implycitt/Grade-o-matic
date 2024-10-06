import cv2
import easyocr

image_path = '../input/math.png'

def read(image_path: str) -> list:
    image = cv2.imread(image_path)
    reader = easyocr.Reader(['en'])
    text = reader.readtext(image)
    read_words = [i[1] for i in text]
    return read_words

words = read(image_path)
print(words)
