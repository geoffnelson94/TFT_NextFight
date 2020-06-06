import sys
import os
import time
from os import path
import pytesseract
import cv2
import pyautogui
from ReadImage import ReadImage
from ProcessImage import ProcessImage
from DetermineOpponent import DetermineOpponent

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def DetermineIfCombat():
    # Find Combat phase
    Combat = 0
    iterator = 0
    max_iter = 50
    while Combat != 1:
        iterator = iterator+1

        # Take a screenshot
        myScreenShot = pyautogui.screenshot()
        myScreenShot.save(r"images\Phase_File.png")

        # Read in image
        img = ReadImage('Phase_File.png')

        # Debug image file
        #print("DEBUG combat phase file")
        #img = ReadImage('Sample_CombatPhase.png')

        # Cropping
        y=160
        h=150
        x=830
        w=300
        img = img[y:y+h, x:x+w]

        # Process image
        img = ProcessImage(img)
        # Show
        #cv2.imshow('Image', img)

        # Text interpret
        text = pytesseract.image_to_string(img)

        # Grab Phase
        current_phase = text.split("\n")

        if (current_phase[0] == 'Planning'):
            print("It's' Planning Phase!")

        if (current_phase[0] == 'Combat'):
            print("It's Combat Phase!")
            DetermineOpponent()

        # Wait a little bit
        time.sleep(0.5)

        # Max iterator
        if (iterator == max_iter):
            print("MAX ITERATOR HIT! Quitting...")
            break
