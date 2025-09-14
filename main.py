import os
import sys
from litellm import completion
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Check if OpenAI API key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        print("Please create a .env file with: OPENAI_API_KEY=your-api-key")
        sys.exit(1)

    print("ChatGPT Console - Type 'quit' to exit")
    print("-" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = completion(
                model="gpt-4o",  # Using GPT-4o as GPT-5 may not be available yet
                messages=[{"content": user_input, "role": "user"}],
                stream=False
            )

            assistant_message = response.choices[0].message.content
            print(f"\nAssistant: {assistant_message}")

        except Exception as e:
            print(f"\nError: {e}")
            print("Please check your API key and internet connection.")


if __name__ == "__main__":
    main()
