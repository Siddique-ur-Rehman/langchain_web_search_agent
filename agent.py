from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_core.tools import Tool
from ddgs import DDGS
import uuid
from chat_history import create_session, save_message, get_messages
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0
)





@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information, news, or real-time data."""
    
    try:
        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    query,
                    max_results=3
                )
            )

        if not results:
            return "No search results found."

        return "\n\n".join(
            f"Title: {r.get('title', '')}\n"
            f"URL: {r.get('href', '')}\n"
            f"Content: {r.get('body', '')}"
            for r in results
        )

    except Exception as e:
        return f"Search failed: {e}"
@tool
def calculate_word_length(word: str) -> int:
    """Returns the exact character count of a given string word."""
    return len(word)


tools = [calculate_word_length,web_search]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="You are a precise assistant. Use tools whenever calculation or verification is required.Also use web search if require for any task."
)



# Create a new session when the program starts
session_id = str(uuid.uuid4())

create_session(session_id)

print(f"Session ID: {session_id}")
print("Type 'quit' to exit.\n")


while True:

    user_input = input("Enter your prompt: ")

    # Check quit before sending anything to the agent
    if user_input.lower() == "quit":
        break

    
    history = get_messages(session_id)

    # Add the current user message
    messages = history + [
        ("user", user_input)
    ]

    # Save user's message
    save_message(
        session_id,
        "user",
        user_input
    )

    # Send conversation history + current message to agent
    response = agent.stream({
        "messages": messages
    })

    assistant_response = ""

    # Stream the agent response
    for chunk in response:

        if "model" in chunk:

            message = chunk["model"]["messages"][-1]

            if message.content:

                print(message.content)

                if message.content:
                    print(message.content)

                if isinstance(message.content, str):
                    assistant_response += message.content

                elif isinstance(message.content, list):
                    for item in message.content:
                        if isinstance(item, dict) and "text" in item:
                            assistant_response += item["text"]

    
    if assistant_response:

        save_message(
            session_id,
            "assistant",
            assistant_response
        )

        print()