from botline.brains.brain import Brain
from loguru import logger

class Bot(object):
    ALIAS = 'UnkownBot'
    
    BIO = """
    I am a highly intelligent question answering bot. If you ask me a 
    question that is rooted in truth, I will give you the answer. If you ask me a 
    question that is nonsense, trickery, or has no clear answer, I will respond 
    with something related but funny.
    """
    
    def __init__(self, brain: Brain) -> None:
        self.set_properties(brain)

    @classmethod
    def set_properties(cls, brain: Brain) -> None:
        cls.brain = brain

    @classmethod
    def alias(cls) -> str:
        return cls.ALIAS

    @classmethod
    def ask(cls, question: str) -> str:
        return cls.brain.answer(question)
