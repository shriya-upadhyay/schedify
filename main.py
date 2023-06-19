# This is a sample Python script.
import os
import openai
import argparse
from config import OPENAI_API_KEY

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="+", type = str, help = "prompt for GPT-3 to complete")
    
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    prompt = "Create an efficient yet feasible one-day schedule for me with the following characteristice: " + prompt
    print(f"Q: {prompt}")
    ask_gpt(prompt)

def ask_gpt(prompt: str):
    openai.api_key = OPENAI_API_KEY
    openai.Model.retrieve("gpt-3.5-turbo-16k-0613")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": prompt},
        ]
)

    content = response['choices'][0]['message']['content']
    content = content.strip()
    print("\033[32m" + content+  "\033[0m")
    return content

if __name__ == "__main__":
    main()



