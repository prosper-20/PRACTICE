import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR"

def convert():
    img = Image.open("download.jfif")
    text = pytesseract.image_to_string(img)
    print(text)

convert()