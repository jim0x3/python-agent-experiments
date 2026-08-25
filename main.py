import argparse
import os
import sys
import json

from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    tools = [{
        "type": "function",
        "function": {
            "name": "Read",
            "description": "Read and return the contents of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to read",
                    }
                },
                "required": ["file_path"],
            },
        },
    }]

    # Messages array
    messages = [{"role": "user", "content": args.p}]

    while True:
        chat = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=tools,
        )

        if not chat.choices or len(chat.choices) == 0:
            raise RuntimeError("no choices in response")
        print("Logs from your program will appear here!", file=sys.stderr)

        # Get the message
        msg = chat.choices[0].message

        if not msg.tool_calls:
            sys.stdout.write((msg.content or "").strip())
            sys.stdout.write("\n")
            break

        messages.append(msg)

        for t in msg.tool_calls:
            if t.function.name == "Read":
                fArgs = json.loads(t.function.arguments)
                with open(fArgs["file_path"], "r") as file:
                    content = file.read()

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": t.id,
                        "content": content,
                    }
                )


if __name__ == "__main__":
    main()
