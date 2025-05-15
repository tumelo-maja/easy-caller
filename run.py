
import os
import openai

# Retrieve the OpenAI API key from environment variable
# openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was successfully retrieved
# if openai_api_key:
#     print("API Key successfully retrieved!")
# else:
#     print("API Key not found!")

from openai import OpenAI

client = OpenAI(
    base_url="https://api.llm7.io/v1",
    api_key="not-needed"  # still required by the client, but can be anything
)

# user_question = input('Enter your question:\n')
user_question= "Say you are awesome Tumelo!"
response = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "user", "content": user_question}
    ]
)

print(response.choices[0].message.content)

