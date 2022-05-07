from loguru import logger

class Brain:
    ALIAS = 'UnkownBrain'
    NO_ANSWER = 'I don\'t know'
        
    @classmethod
    def alias(cls):
        return cls.ALIAS
    
    @classmethod
    def answer(cls, question: str):
        return cls.NO_ANSWER