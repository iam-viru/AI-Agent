from openai import OpenAI
from dotenv import load_dotenv
import os
print("=" *40)
#Load configuration from .env file
load_dotenv();
#Create a client that communicates with Ollama
client=OpenAI(base_url=os.getenv("Base_URL"), api_key=os.getenv("API_KEY"))

#Send a question to the AI model
response=client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":"What is Artificatial Intelligence?"
        }
    ]
)   
print(response.choices[0].message.content)
