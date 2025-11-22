import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_audio_tts_and_transcription():
    print("--- Testing Audio (TTS & Transcription) ---")
    speech_file_path = Path(__file__).parent / "speech.mp3"
    text_input = "The quick brown fox jumps over the lazy dog."
    
    # 1. Text to Speech
    print("Generating speech...")
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text_input
        )
        response.stream_to_file(speech_file_path)
        print(f"Speech saved to {speech_file_path}")
    except Exception as e:
        print(f"Error in TTS: {e}")
        return

    # 2. Transcription
    print("Transcribing speech...")
    try:
        with open(speech_file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        print(f"Original Text: {text_input}")
        print(f"Transcribed Text: {transcription.text}\n")
    except Exception as e:
        print(f"Error in Transcription: {e}")

if __name__ == "__main__":
    test_audio_tts_and_transcription()
