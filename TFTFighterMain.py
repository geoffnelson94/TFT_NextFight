import pyautogui
import cv2
from DeterminePlayerNames import DeterminePlayerNames
from DetermineIfCombat import DetermineIfCombat
print('TFTFighterNext Software Starting Up!')

# Determine players
DeterminePlayerNames()

# Determine if it's a combat phase
DetermineIfCombat()

# Wait to quit
cv2.waitKey(0)
