import cv2
import os
import subprocess
import os
import numpy as np

def capture_image(file_path):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # Apply a Gaussian blur to the frame
        blurred_frame = cv2.GaussianBlur(frame, (21, 21), 0)
        
        # Convert the blurred frame to grayscale for desaturation
        gray_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2GRAY)
        
        # Convert the grayscale frame back to BGR (still looks gray)
        desaturated_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        
        # Save the processed image
        cv2.imwrite(file_path, desaturated_frame)
    cap.release()

# Use this in the rest of your script where you handle the file path
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, "processed_image.jpg")

# Now when you call capture_image it will save a blurred and desaturated image
capture_image(file_path)

def set_background(file_path):
    # Set the captured image as desktop background
    script = f'''
    tell application "System Events"
        set desktopCount to count of desktops
        repeat with desktopNumber from 1 to desktopCount
            tell desktop desktopNumber
                set picture to "{file_path}"
            end tell
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script], text=True)

set_background(file_path)

