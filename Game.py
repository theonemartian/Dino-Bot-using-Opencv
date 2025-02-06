# Python program for automating the Chrome Dinosaur Game using OpenCV
# The program detects obstacles using color detection and automatically makes the dinosaur jump

import cv2
import numpy as np
import pyautogui
import time

def press_space():
    '''Makes the dinosaur jump by simulating a space key press'''
    # Release the down key if it was pressed
    pyautogui.keyUp('down')

    # Press space to make the dinosaur jump
    pyautogui.keyDown('space')

    # Small delay to ensure the space key press is registered
    time.sleep(0.05)

    # Additional delay for jump animation
    time.sleep(0.10)

    # Release the space key after jump
    pyautogui.keyUp('space')

    # Press down key again to maintain crouching position
    pyautogui.keyDown('down')

# Initialize video capture from webcam
url="https://xyz/video"
cap = cv2.VideoCapture(0)
x = 0  # Counter variable for consecutive detections

# Set video capture resolution
cap.set(3, 620)  # Width
cap.set(4, 480)  # Height

# Main game loop
while True:
    # Capture frame-by-frame from the video stream
    _, frame = cap.read()

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # Convert from BGR to HSV color space for better color detection
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Define the HSV color range for obstacle detection
    lower_red = np.array([33, 232, 230])
    upper_red = np.array([180, 255, 255])

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply the mask to the original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # If obstacle is detected (color in range is found)
    if res.any():
        x = x + 1
        press_space()
    else:
        x = 0

    # Check for 'ESC' key press to exit
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Clean up resources
cv2.destroyAllWindows()
cap.release()