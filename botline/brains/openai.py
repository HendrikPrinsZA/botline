import json
import os
from dotenv import load_dotenv
import openai
from botline.brains.brain import Brain
from botline.cache import Cache
from botline.definitions import PROJ_DIR, ROOT_DIR

class OpenAi(Brain):
    ALIAS = 'OpenAI'
    NO_ANSWER = 'has no response'

    def __init__(self) -> None:
        super().__init__()

        self.path_env = f"{PROJ_DIR}/.env"
        self.path_cache = f"{PROJ_DIR}/.cache/openai.json"
        
        self.cache = Cache(self.path_cache)
        load_dotenv(self.path_env)
        openai_key = os.getenv("OPEN_AI_API_KEY")
        
        if openai_key is None:
            print("Error: Expected env variable 'OPEN_AI_API_KEY' not found")
            exit(1)

        openai.api_key = openai_key

    def answer(self, text: str) -> str:
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

        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = prompt,
            temperature = 0.7,
            max_tokens = 100,
            top_p = 1,
            frequency_penalty = 0.2,
            presence_penalty = 0,
        )
        
        return self.cache.set(prompt, response)
