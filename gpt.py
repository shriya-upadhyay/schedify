import os
import openai
from config import OPENAI_API_KEY


def ask_gpt(prompt: str):
    prompt = "Create an efficient yet feasible and reasonable detailed one-day schedule for me with the following restrictions in the format 'time' ~ 'activity': " + prompt
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

    schedule_dict = {}
    lines = content.split("\n")

    for line in lines:
        parts = line.strip().split(" ~ ")

        if len(parts) == 2:
            time = parts[0]
            activity = parts[1]

            schedule_dict[time] = activity

    #print(content)
    return schedule_dict
