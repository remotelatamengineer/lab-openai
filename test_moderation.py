import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_moderation():
    print("--- Testing Moderation ---")
    text_to_check = "I want to kill them."
    try:
        response = client.moderations.create(input=text_to_check)
        output = response.results[0]
        print(f"Text: {text_to_check}")
        print(f"Flagged: {output.flagged}")
        if output.flagged:
            print("Categories:")
            for category, flagged in output.categories:
                if flagged:
                    print(f"- {category}")
        print("\n")
    except Exception as e:
        print(f"Error in Moderation: {e}")

if __name__ == "__main__":
    test_moderation()
