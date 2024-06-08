import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
import click

load_dotenv()
os.environ["OPENAI_API_KEY"]

client = OpenAI()

@click.command()
def chat_with_felix():
    """Chat with Felix, the chatbot."""
    print("Felix: Hi there. I am Felix, the chatbot. How can I help you today?")
    
    while True:  # This will keep the chat session active
        message = input("You: ")

        # Exit the loop (and the program) if the user types 'exit' or '\quit'
        if message.lower() in ['exit', 'quit']:
            print("Felix: Goodbye!")
            break

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are smart and helpful assistant."},
                {"role": "user", "content": "Hi there."},
                {"role": "assistant", "content": "Hi there. \n\nI am Felix, the chatbot.\n\nHow can I help you today?"},
                {"role": "user", "content": f"{message}"},
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        try:
            print("Felix:", response.choices[0].message.content)
        except:
            print("Felix: Sorry, a problem occurred. Please try again later.")

if __name__ == '__main__':
    chat_with_felix()
