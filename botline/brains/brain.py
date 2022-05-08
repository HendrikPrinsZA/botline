from loguru import logger

class Brain(object):
    ALIAS = 'UnkownBrain'
    NO_ANSWER = 'has no answer'
        
    @classmethod
    def alias(cls) -> str:
        return cls.ALIAS
    
    @classmethod
    def answer(cls, question: str) -> str:
        return cls.no_answer()
    
    @classmethod
    def no_answer(cls) -> str:
        return cls.NO_ANSWER