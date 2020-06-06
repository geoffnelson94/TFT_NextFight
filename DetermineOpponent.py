import sys
import os
import time
from os import path
import pytesseract
import cv2
from cv2.cv2 import cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY
import pyautogui
import numpy as np

from ReadImage import ReadImage
from ProcessImage import ProcessImage

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def DetermineOpponent():

    # Wait for opponent to load
    time.sleep(1)
    Opponent = [""]
    iter = 0
    max_iter = 3
    while Opponent[0] == '':
        iter = iter + 1
        # Take a screenshot
        myScreenShot = pyautogui.screenshot()
        myScreenShot.save(r"images\Opponent_File.png")

        # Read in image
        img  = ReadImage('Opponent_File.png')

        # Debug opponent image
        #img = ReadImage('Sample_Opponent2.png')

        # Cropping
        y=20
        h=45
        x=1220
        w=300
        img = img[y:y+h, x:x+w]

        # Process image
        #img = ProcessImage(img)

        # Grayscale
        img = cvtColor(img,COLOR_BGR2GRAY)

        # Color thresholding
        _,img = threshold(img,160,255,THRESH_BINARY)
        img = cv2.bitwise_not(img) # Invert black/white
        # Sharpen
        sharpening_kernal = np.array([[-1,-1,-1],
                                      [-2, 11 ,-2],
                                      [-1,-1,-1]])

        img = cv2.filter2D(img, -1, sharpening_kernal)



        # Show
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyWindow('Image')

        # Text interpret
        text = pytesseract.image_to_string(img)

        # Grab Phase
        Opponent = text.split("\n")
        print(Opponent)

        if(iter == max_iter):
            print("Done trying to find opponents!")
            break
