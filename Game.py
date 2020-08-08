
# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import cv2 
import numpy as np  
import pyautogui 
import time 

def press_space(): 
   
    # releasing the Down Key  
    pyautogui.keyUp('down')  
  
    # pressing Space to overcome Bush 
    pyautogui.keyDown('space') 
  
    # so that Space Key will be recognized easily 
    time.sleep(0.05)  
  
    # printing the "Jump" statement on the 
    # terminal to see the current output  
     
    time.sleep(0.10) 
  
    # releasing the Space Key  
    pyautogui.keyUp('space') 
  
    # again pressing the Down Key to keep my Bot always down  
    pyautogui.keyDown('down') 
# Webcamera no 0 is used to capture the frames 
url="https://xyz/video"
cap = cv2.VideoCapture(0)
x=0
cap.set(3,620)
cap.set(4,480)


  
# This drives the program into an infinite loop. 
while True:        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    

    # Converts images from BGR to HSV 
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) 
    
    

    lower_red = np.array([33,232,230]) 
    upper_red = np.array([180,255,255]) 
  
    # Here we are defining range of bluecolor in HSV 
    # This creates a mask of blue coloured  
    # objects found in the frame. 
    mask = cv2.inRange(hsv, lower_red, upper_red) 

    # The bitwise and of the frame and mask is done so  
    # that only the blue coloured objects are highlighted  
    # and stored in res 
    
    
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    if res.any():
        x=x+1
        press_space()
        
        
        
    else:
        x=0
        

    # This displays the frame, mask  
    # and res which we created in 3 separate windows. 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
     
      
     
# D   estroys all of the HighGUI wind o ws.
cv2.destroyAllWindows()    
        
# relea se the captured frame q
cap.release()     
