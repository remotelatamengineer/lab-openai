import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_image_generation():
    print("--- Testing Image Generation ---")
    prompt = "A cute baby sea otter wearing a beret"
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        print(f"Prompt: {prompt}")
        print(f"Image URL: {image_url}\n")
    except Exception as e:
        print(f"Error in Image Generation: {e}")

if __name__ == "__main__":
    test_image_generation()
