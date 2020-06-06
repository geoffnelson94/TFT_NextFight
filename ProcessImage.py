import cv2
from cv2.cv2 import cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY
import numpy as np

def ProcessImage(Image):

    # Grayscale
    img = cvtColor(Image,COLOR_BGR2GRAY)

    # Color thresholding
    _,img = threshold(img,130,255,THRESH_BINARY)
    img = cv2.bitwise_not(img) # Invert black/white
    # Sharpen
    sharpening_kernal = np.array([[-1,-1,-1],
                                  [-2, 11 ,-2],
                                  [-1,-1,-1]])

    img = cv2.filter2D(img, -1, sharpening_kernal)
    return img
