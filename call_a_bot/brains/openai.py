from call_a_bot.brains.brain import Brain

class OpenAi(Brain):
    ALIAS = 'OpenAI'
    
    def __init__(self):
        super().__init__()
    
    def answer(self, question: str):
        return self.NO_ANSWER

    @classmethod
    def alias(cls):
        return cls.ALIAS