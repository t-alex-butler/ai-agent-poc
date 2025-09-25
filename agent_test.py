from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
from typing import Optional


load_dotenv()  # read .env into environment
API_KEY_ENV = "OPENAI_API_KEY"


def get_client() -> OpenAI:
    """Create and return an OpenAI client using the API key from env.

    Raises:
        SystemExit: if the API key is missing.
    """
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        print(f"{API_KEY_ENV} not found in environment. Set it in .env or the shell.")
        raise SystemExit(1)
    return OpenAI(api_key=api_key)


def chat_loop(client: Optional[OpenAI] = None) -> None:
    """Simple REPL that sends user input to the OpenAI chat completions API.

    The loop exits on input 'exit' or 'quit'.
    """
    if client is None:
        client = get_client()

    print("AI Agent ready! Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            return

        try:
            resp = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": user_input}],
            )
        except Exception as e:  # keep broad for user convenience in this small script
            print("Error contacting API:", str(e))
            continue

        # Safely extract content
        try:
            content = resp.choices[0].message.content
        except Exception:
            content = str(resp)

        print("Agent:", content)


if __name__ == "__main__":
    try:
        client = get_client()
    except SystemExit:
        sys.exit(1)
    chat_loop(client)