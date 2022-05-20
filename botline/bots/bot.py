from botline.brains.brain import Brain

class Bot(object):
    ALIAS = 'UnkownBot'
    
    BIO = None

    BIO_MESSAGES = []
    
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
