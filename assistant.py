from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import(get_current_time,roll_dice,generate_password)

# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("Base_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)
 
while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAI :", response.choices[0].message.content)

