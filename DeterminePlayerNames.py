import sys
import os
from os import path
import pytesseract
import cv2
import pyautogui
import time
from ReadImage import ReadImage
from ProcessImage import ProcessImage
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def DeterminePlayerNames():

    # Take a screenshot
    myScreenShot = pyautogui.screenshot()
    myScreenShot.save(r"images\PlayerNames_File.png")

    # Read Image
    img = ReadImage("PlayerNames_File.png")

    # Cropping for player names
    y=120
    h=700
    x=1650
    w=178
    img = img[y:y+h, x:x+w]

    # Process image
    img = ProcessImage(img)
    # Show
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Image')
    # Text interpret
    text = pytesseract.image_to_string(img)

    # Split and filter text
    text = text.split("\n") # Split text by new lines
    text = [string for string in text if string != ""] # Get rid of empty strings
    player_list = [string for string in text if len(string) > 2] # Get rid of strings < 2 in size (Assumption)

    # Get player names
    #player_list = [string for string in player_list if not string.isdigit()]
    #health_list = [string for string in ]
    print ("Looks like we'll be fighting:")
    print(player_list)
