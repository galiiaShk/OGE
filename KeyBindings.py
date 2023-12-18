import cv2
import mediapipe as mp
import keyboard 
import numpy as np
import json
#variables 

cap= cv2.VideoCapture(0)

hands= mp.solutions.hands.Hands(static_image_mode=False,
                        max_num_hands=1,
                        min_tracking_confidence=0.5,
                        min_detection_confidence=0.5)

mpDraw = mp.solutions.drawing_utils


def quit(): 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows()
        return True    
#---------------------------------------
# reads the handcoordinates on the "r"-Key
def readCoords(init, savedFilePath):
    if keyboard.is_pressed('r')|init:
        f = open(savedFilePath,"r")
        result= f.read()
        f.close()
        res = json.loads(result)
        return res
#---------------------------------------
#writes  the handcoordinates on the "w"-Key
def writeCoords(recognizedPoints, savedFilePath):
     if keyboard.is_pressed('w'): 
        f = open(savedFilePath,"w")
        f.write(str(recognizedPoints)) 
        f.close()      
#---------------------------------------     