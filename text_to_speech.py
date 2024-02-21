from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with your API key
openai = OpenAI(api_key=api_key)

def text_to_speech(text):
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        audio_file_path = os.path.join("audio-outputs", "speech.mp3")
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
        return audio_file_path
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None

# The function can be tested directly by uncommenting the following lines:
# if __name__ == "__main__":
#    result = text_to_speech("Hello, this is a test of the text to speech conversion.")
#    print(f"Speech file generated at: {result}")