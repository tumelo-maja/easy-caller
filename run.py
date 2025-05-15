
import os
import openai

# Retrieve the OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was successfully retrieved
if openai_api_key:
    print("API Key successfully retrieved!")
else:
    print("API Key not found!")


# Retrieve the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Example request to the OpenAI API (using GPT-3)
response = openai.completions.create(
  engine="text-davinci-003",
  prompt="What is the capital of France?",
  max_tokens=50
)

# Print the response
# print(response.choices[0].text.strip())