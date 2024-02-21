import cv2
import time
import base64
from openai import OpenAI
import os
from text_to_speech import text_to_speech

# Initialize OpenAI client with your API key
openai = OpenAI(api_key="your_openai_api_key_here")

def capture_image():
    cam = cv2.VideoCapture(0)
    time.sleep(2)  # Warm-up time
    ret, frame = cam.read()
    cam.release()
    
    if not ret:
        print("Failed to capture image.")
        return None
    
    return frame

def encode_image_to_base64(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer).decode('utf-8')

def process_image_with_gpt4(image_base64):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[{
                "role": "user",
                "content": [{"type": "image", "data": f"data:image/jpeg;base64,{image_base64}"}]
            }],
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error processing image with GPT-4: {e}")
        return None

def main():
    frame = capture_image()
    if frame is not None:
        image_base64 = encode_image_to_base64(frame)
        text_description = process_image_with_gpt4(image_base64)
        if text_description:
            print("Generated Text:", text_description)
            speech_file = text_to_speech(text_description)
            print(f"Generated speech saved to {speech_file}")
        else:
            print("No description was generated.")
    else:
        print("Image capture failed.")

if __name__ == "__main__":
    main()
