import os
from dotenv import load_dotenv
import openai

SCRIPT_DIR = os.path.realpath(__file__).replace('/main.py', '')
load_dotenv(f"{SCRIPT_DIR}/.env")
CACHE_PATH = f"{SCRIPT_DIR}/cache.json"

class OpenAiAPI:
  ALIAS = 'OpenAI'

  PARAMS = {
    'engine': 'text-davinci-002',
    'temperature': 0.7,
    'max_tokens': 100,
    'top_p': 1,
    'frequency_penalty': 0.2,
    'presence_penalty': 0
  }

  def __init__(self):
    openai.api_key = os.getenv("OPEN_AI_API_KEY")

    self.completion = openai.Completion()


