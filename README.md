****Humorous Storyteller with Image Capturing****

This project integrates image capturing, AI-powered storytelling, and text-to-speech conversion to create an engaging and humorous narrative based on images captured in real-time. Utilizing OpenAI's GPT-4 for generating stories and its text-to-speech capabilities, the system captures images from a webcam, generates a story for each image, and narrates the story aloud, providing a seamless, entertaining experience.

**Features**

Image Capturing: Uses a webcam to capture images continuously.
AI-Driven Storytelling: Leverages OpenAI's GPT-4 API to generate humorous stories based on the captured images.
Text-to-Speech Conversion: Converts the generated stories into speech, narrating them aloud.
Continuous Operation: Runs in a loop, capturing images and generating new story parts without manual intervention until stopped.

**Getting Started**
Prerequisites
Python 3.x
OpenAI API Key
Webcam

**Installation**
Clone the repository:
git clone github.com/vittoriohalfon/live-storytelling.git
cd your-repository-directory

Install required Python packages:
pip install -r requirements.txt

Create a .env file in the project root directory and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

Create a audio-outputs/ directory in the project's root directory:
mkdir audio-outputs

**Usage**
Run the script to start the image capturing and storytelling loop:
python3 script-pic.py

The system will begin capturing images, generating stories, and narrating them. Press CTRL+C to exit the loop.

**Configuration**
Image Capture Delay: Adjust the sleep duration in script-pic.py to control how frequently images are captured.
Story Length: Modify the max_tokens parameter in process_image_with_gpt4 function to change the length of the generated stories.
Text-to-Speech Voice: Change the voice parameter in the text_to_speech function to select different narrator voices.

**Troubleshooting**
API Key Issues: Ensure your .env file is correctly set up with a valid OpenAI API key.
Webcam Access: If image capturing fails, check that your webcam is properly connected and accessible by the script.
Audio Playback: Ensure your system's audio output is correctly configured if you encounter issues with speech narration.
