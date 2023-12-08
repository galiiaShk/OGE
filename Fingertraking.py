#pip install opencv-python
#pip install mediapipe
#pip install --user numpy --upgrade

import numpy as np
import cv2
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands(static_image_mode=False,
                         max_num_hands=2,
                         min_tracking_confidence=0.5,
                         min_detection_confidence=0.5)

mpDraw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0

while True:
    _, img = cap.read()
    result = hands.process(img)
    #print(result)
    
    if result.multi_hand_landmarks:
        #for hand in result.multi_hand_landmarks:
        
        for id, lm in enumerate(result.multi_hand_landmarks[0].landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 3, (128, 128, 128))
            
            #Marks the top of fingers with different colors and thickness
            if id == 4:
                cv2.circle(img, (cx, cy), 6, (0, 0, 0), cv2.FILLED)
            if id == 8:
                cv2.circle(img, (cx, cy), 12, (255, 0, 0), cv2.FILLED)
            if id == 12:
                cv2.circle(img, (cx, cy), 12, (0, 255, 0), cv2.FILLED)
            if id == 16:
                cv2.circle(img, (cx, cy), 12, (0, 0, 255), cv2.FILLED)
            if id == 20:
                cv2.circle(img, (cx, cy), 12, (255, 0, 255), cv2.FILLED)
               
            #print(id)
            #print(lm)
            
            mpDraw.draw_landmarks(img, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
            
            #Shows Frames per Second
            currentTime = time.time()
            fps = 1/(currentTime-previousTime)
            previousTime = currentTime
            
            cv2.putText(img, str(int(fps)), (10, 10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) #Pos,Font,Scale,Color,Thick
            


    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)