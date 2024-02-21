from dotenv import load_dotenv
import os
import cv2
import time
import base64
from openai import OpenAI
from text_to_speech import text_to_speech

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with your API key
openai = OpenAI(api_key=api_key)

client = OpenAI()

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

def process_image_with_gpt4(image_base64, prompt_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]
            }],
            max_tokens=50
        )
        text_description = response.choices[0].message.content
        return text_description
    except Exception as e:
        print(response)
        print(f"Error processing image with GPT-4: {e}")
        return None

def main():
    story_context = []

    while True:
        frame = capture_image()
        if frame is not None:
            image_base64 = encode_image_to_base64(frame)

            # Check if there's existing story context to append to
            if story_context:
                prompt_text = "Continue the funny story based on this image and the previous part: " + story_context[-1]
            else:
                prompt_text = "Start a funny story based on this image."

            text_description = process_image_with_gpt4(image_base64, prompt_text)

            if text_description:
                print("Generated Text:", text_description)
                story_context.append(text_description) # Append to story context
                speech_file = text_to_speech(text_description)
                print(f"Generated speech saved to {speech_file}")
            else:
                print("No description was generated.")
        else:
            print("Image capture failed.")

        # Check if the user wants to continue or break the loop
        if input("Press Enter to capture another image or type 'quit' to exit: ").lower() == 'quit':
            break

if __name__ == "__main__":
    main()
