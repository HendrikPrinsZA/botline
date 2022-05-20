import json
import os
from dotenv import load_dotenv
import nlpcloud
from botline.brains.brain import Brain
from botline.cache import Cache
from botline.definitions import PROJ_DIR

class NlpCloud(Brain):
    ALIAS = 'NlpCloud'
    NO_ANSWER = 'has no response'

    def __init__(self) -> None:
        super().__init__()

        self.path_env = f"{PROJ_DIR}/.env"
        self.path_cache = f"{PROJ_DIR}/.cache/nlpcloud.json"
        
        self.cache = Cache(self.path_cache)
        load_dotenv(self.path_env)

        key = os.getenv("NLP_CLOUD_API_KEY")
        
        if key is None:
            print("Error: Expected env variable 'NLP_CLOUD_API_KEY' not found")
            exit(1)

        self.client = nlpcloud.Client("fast-gpt-j", key, True)

    def answer(self, text: str) -> str:
        print("Unsupported: NlpCloud still in development")
        exit(1)
        return self.get_answer(text)

    def get_answer(self, prompt) -> str:
        response = self.get_reponse(prompt)

        text = ""
        try:
            text = str(response['choices'][0]['text'])
        except:
            print("Error: Unexpected response from OpenAI")
            print(response)
            exit(1)

        return text

    def get_reponse(self, prompt) -> json:
        response = self.cache.get(prompt)
        if response is not None:
            return response

        response = self.client.question(
            "Example context",
            "When was the Guardian created?"
        )
        
        return self.cache.set(prompt, response)
