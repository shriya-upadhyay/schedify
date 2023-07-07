# This is a sample Python script.
import os
import openai
import argparse
from config import OPENAI_API_KEY
from website import create_app
from gpt import ask_gpt

app = create_app()



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="+", type = str, help = "prompt for GPT-3 to complete")
    
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    prompt = "Create an efficient yet feasible one-day schedule for me with the following characteristice: " + prompt
    print(f"Q: {prompt}")
    #ask_gpt(prompt)


if __name__ == '__main__':
    app.run(debug=True)
    main()





