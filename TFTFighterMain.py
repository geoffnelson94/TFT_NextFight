import pyautogui
import pytesseract
import cv2
import sys
import os
from os import path
from cv2.cv2 import cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY
print('TFTFighterNext Software Starting Up!')


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Take a screenshot
myScreenShot = pyautogui.screenshot()
myScreenShot.save(r"images\myFile.png")

# Read in image
if not(path.isfile('images/myFile.png')):
    print("Image file not found!")

img = cv2.imread('images\Sample.png')

# Process
image = cvtColor(img,COLOR_BGR2GRAY)
#_,image = threshold(image,177,255,THRESH_BINARY)
cv2.imshow("TEST",image)
cv2.waitKey(0)
text = pytesseract.image_to_string(image, lang='eng')
print(text)

# Do stuff
