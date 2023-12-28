from pathlib import Path
import subprocess
import cv2
import os
import numpy as np
import subprocess
import time

# Your image file path
image_path = '/Users/chase/Code/live-bg/processed_image.jpg'

# Run the Shortcut with the image file as input


def capture_image(file_path):
    cap = cv2.VideoCapture(0)
    # Give the camera some time to warm up
    time.sleep(2)  # 2 second delay to allow the camera to warm up
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        # Apply a very strong Gaussian blur to the frame
        blurred_frame = cv2.GaussianBlur(frame, (101, 101), 0)
        
        # Convert the blurred frame to grayscale
        gray_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2GRAY)
        
        # Convert the grayscale frame back to BGR
        gray_frame_colored = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        
        # Blend the grayscale frame with the original frame for partial desaturation
        desaturated_frame = cv2.addWeighted(blurred_frame, 0.9, gray_frame_colored, 0.1, 0)
        
        # Save the processed image
        cv2.imwrite(file_path, desaturated_frame)
    else:
        print("Failed to capture image from webcam.")


def set_wallpaper(file_path):
    image_path = Path(file_path).absolute()
    applescript = f"""
    tell application "Finder"
        set desktop picture to POSIX file "{image_path}"
    end tell
    """
    try:
        subprocess.call(["osascript", "-e", applescript])
        print("Wallpaper set successfully.")
    except subprocess.CalledProcessError as error:
        print(f"Error setting wallpaper: {error}")

# Use this in the rest of your script where you handle the file path
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, "processed_image.jpg")

capture_image(file_path)


# Your image file path
image_path = file_path

# # Run the Shortcut with the image file as input
subprocess.run(['shortcuts', 'run', 'Set Wallpaper', '--input-path', image_path])
# set_wallpaper(file_path)
