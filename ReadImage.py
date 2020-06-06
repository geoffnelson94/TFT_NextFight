import cv2
from os import path

def ReadImage(Image):
    # Read in image
    if not(path.isfile('images/%s' %Image)):
        print("Image file not found!")

    img = cv2.imread('images/%s' %Image)

    # Check image params
    height, width, trash = img.shape
    if(height != 1080):
        print("Unexpected screen resolution!")
    if (width != 1920):
        print("Unexpected screen resolution!")
    return img
