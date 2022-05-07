# from call_a_bot.brains.brain import Brain
from loguru import logger
from call_a_bot.brains.brain import Brain

class OpenAi(Brain):
    ALIAS = 'OpenAI'
    
    def answer(self, question: str):
        # message = f"{self.ALIAS} is thinking internally about {question}..."
        # logger.info(message)
        
        return "I don't have an answer"

    @classmethod
    def alias(cls):
        return cls.ALIAS