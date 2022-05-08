import os
from dotenv import load_dotenv
from loguru import logger
import openai
from botline.brains.brain import Brain

class OpenAi(Brain):
    ALIAS = 'OpenAI'
    NO_ANSWER = 'has no response'

    def __init__(self) -> None:
        super().__init__()
        path_env = os.path.abspath(f"{os.path.dirname(__file__)}/../../.env")
        load_dotenv(path_env)
        openai_key = os.getenv("OPEN_AI_API_KEY")
        
        if openai_key is None:
            logger.error(f"Expected env variable 'OPEN_AI_API_KEY' not found")
            exit(1)

        openai.api_key = openai_key

    def answer(self, prompt: str) -> str:
        return self.get_answer(prompt)

    def get_answer(self, prompt) -> str:
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = prompt,
            temperature = 0.7,
            max_tokens = 100,
            top_p = 1,
            frequency_penalty = 0.2,
            presence_penalty = 0,
        )

        text = ""
        try:
            text = str(response.choices[0].text)
        except:
            logger.error(f"Unexpected or no response from OpenAI")
            exit(1)
        
        return text