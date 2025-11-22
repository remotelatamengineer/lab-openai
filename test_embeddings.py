import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_embeddings():
    print("--- Testing Embeddings ---")
    text = "OpenAI is an AI research and deployment company."
    try:
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        embedding = response.data[0].embedding
        print(f"Text: {text}")
        print(f"Embedding length: {len(embedding)}")
        print(f"First 5 dimensions: {embedding[:5]}\n")
    except Exception as e:
        print(f"Error in Embeddings: {e}")

if __name__ == "__main__":
    test_embeddings()
