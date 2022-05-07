import time
from loguru import logger

class Brain:
  ALIAS = 'UnkownBrain'
    
  @classmethod
  def whoami(self):
    return "I am {self.ALIAS}"
  
  @classmethod
  def answer(self, question: str):
    message = f"{self.ALIAS} is thinking about {question}..."
    logger.info(message)
    return "I don't have an answer"