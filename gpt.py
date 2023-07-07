import os
import openai
from config import OPENAI_API_KEY


def ask_gpt(prompt: str):
    prompt = "Create an efficient yet feasible one-day schedule for me with the following characteristics: " + prompt
    openai.api_key = OPENAI_API_KEY
    openai.Model.retrieve("gpt-3.5-turbo-16k-0613")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": prompt},
        ]
    )

    content = response['choices'][0]['message']['content']
    #content = content.strip()
    #print("\033[32m" + content+  "\033[0m")

    print(content)
    return content