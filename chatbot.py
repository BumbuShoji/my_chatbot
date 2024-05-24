import openai
import os

# Load the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the chat function
class Chatbot:
    def __init__(self):
        self.chatbot = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
            ],
        )

    def chat(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            max_tokens=150,
        )
        return response.choices[0].message["content"]