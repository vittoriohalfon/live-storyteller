import threading
import queue
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

# Initialize a queue for audio file paths
audio_queue = queue.Queue()

# Worker function to play audio files from the queue
def audio_player():
     while True:
        audio_file_path = audio_queue.get() #Wait for an audio file to be added to the queue
        playsound(audio_file_path) #Play the audio file
        audio_queue.task_done() #Mark the task as done

# Start the audio player thread
threading.Thread(target=audio_player, daemon=True).start()

def play_audio_async(audio_file_path):
        # Add the audio file path to the queue
        audio_queue.put(audio_file_path)

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
        play_audio_async(audio_file_path)
        return audio_file_path
    
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None

# The function can be tested directly by uncommenting the following lines:
# if __name__ == "__main__":
#    result = text_to_speech("Hello, this is a test of the text to speech conversion.")
#    print(f"Speech file generated at: {result}")