import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_chat_completion():
    print("--- Testing Chat Completion ---")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Tell me a short joke."}
            ]
        )
        print(f"Response: {response.choices[0].message.content}\n")
    except Exception as e:
        print(f"Error in Chat Completion: {e}")

def test_chat_stream():
    print("--- Testing Chat Completion (Streaming) ---")
    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Count to 5."}
            ],
            stream=True,
        )
        print("Response: ", end="")
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        print("\n")
    except Exception as e:
        print(f"Error in Chat Stream: {e}")

if __name__ == "__main__":
    test_chat_completion()
    test_chat_stream()
