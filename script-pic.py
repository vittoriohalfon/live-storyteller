import cv2
import schedule
import time
import base64
import os

def capture_image():
    # Initialize the webcam
    cam = cv2.VideoCapture(0)
    
    # Capture a single frame
    ret, frame = cam.read()
    if ret:
        # Specify the image path
        image_path = f"selfie_{int(time.time())}.png"
        # Save the image
        cv2.imwrite(image_path, frame)
        
        # Optionally, encode the image to base64 for API submission
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            print(base64_image)  # You can then use this for your API request
        
        # Clean up
        print(f"Captured {image_path}")
    else:
        print("Failed to capture image.")
    
    # Release the webcam
    cam.release()

# Schedule the capture function every 5 seconds
schedule.every(5).seconds.do(capture_image)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
