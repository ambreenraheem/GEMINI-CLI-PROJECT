from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get the Gemini API key from the environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# IMPORTANT: Make sure you have a .env file with your Gemini API key.
# The .env file should contain a line like:
# GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

if not GEMINI_API_KEY or GEMINI_API_KEY == "GEMINI_API_KEY":
    print("GEMINI_API_KEY not found or not set in .env file.")
    print("Please create a .env file and add your API key in the format:")
    print('GEMINI_API_KEY="GEMINI_API_KEY"')
    exit()


# Initialize the OpenAI client with the Gemini API endpoint
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

# Make a chat completion request
try:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain to me how AI works"},
        ],
    )

    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    if "401" in str(e):
        print(
            "This might be due to an invalid API key. Please check your API key and try again."
        )
