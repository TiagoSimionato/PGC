from pytesseract import pytesseract
import cv2
import numpy as np

TESSERACT_PATH = r"D:\Arquivos de Programas HD\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = TESSERACT_PATH

imagePath = './images/7.jpeg'
# imagePath = './images/2_small.jpeg'
# imagePath = './images/test.jpg'
# imagePath = './images/clock.jpeg'
# imagePath = './images/calculator.jpeg'
# imagePath = './images/numbers.jpeg'
# imagePath = './images/calculator2.jpg'
# imagePath = './images/test.png'

img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
inverted = cv2.bitwise_not(img);
# thresh = 128
# kernel = np.ones((3, 3), np.uint8) 
# binary = cv2.threshold(inverted, thresh, 255, cv2.THRESH_BINARY)[1]


ocrImage = inverted
text = pytesseract.image_to_string(ocrImage, config='--psm 10')
print(text)


# img = cv2.imread('./images/calculator.jpeg')
# gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', ocrImage)
cv2.waitKey(0)

# mser = cv2.MSER().create()
# regions = mser.detectRegions(image=gray)
# [print(p.size) for p in regions]
# hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
# cv2.polylines(gray, hulls, 1, (0, 0, 255), 2)
# cv2.imshow('image', img)
# cv2.waitKey(0)