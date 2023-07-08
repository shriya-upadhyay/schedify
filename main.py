# This is a sample Python script.
import os
import openai
import argparse
from config import OPENAI_API_KEY
from website import create_app
from gpt import ask_gpt

app = create_app()
    


if __name__ == '__main__':
    app.run()





