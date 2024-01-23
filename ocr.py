from pytesseract import pytesseract

TESSERACT_PATH = r"D:\Arquivos de Programas HD\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = TESSERACT_PATH

text = pytesseract.image_to_string('./images/test.png')
print(text)