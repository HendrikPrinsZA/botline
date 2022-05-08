from loguru import logger
from call_a_bot.brains.brain import Brain

class Terminal(Brain):
    ALIAS = 'Terminal'
    NO_ANSWER = 'is not available'
    
    def answer(self, question: str) -> str:
        try:
            answer = input(question)
        except:
            exit()
        
        if len(answer) == 0:
            return self.answer(question)

        return answer