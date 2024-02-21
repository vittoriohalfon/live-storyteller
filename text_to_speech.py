import threading
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from playsound import playsound
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with your API key
openai = OpenAI(api_key=api_key)

def play_audio_async(audio_file_path):
        playsound(audio_file_path)

def text_to_speech(text):
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        # Generate unique filename through timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        audio_file_path = os.path.join("audio-outputs", f"speech_{timestamp}.mp3")

        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)

        # Play audio in a separate thread
        threading.Thread(target=play_audio_async, args=(audio_file_path,)).start()
        return audio_file_path
    
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None

# The function can be tested directly by uncommenting the following lines:
# if __name__ == "__main__":
#    result = text_to_speech("Hello, this is a test of the text to speech conversion.")
#    print(f"Speech file generated at: {result}")
