import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize model
llm = ChatOpenAI(
    model="gpt-4o-mini",  # free/cheap tier model for now
    temperature=0.2
)

def main():
    print("🤖 AI Dev Agent started!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = llm.invoke(user_input)
        print("Agent:", response.content)

if __name__ == "__main__":
    main()
