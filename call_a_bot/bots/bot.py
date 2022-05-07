from call_a_bot.brains.brain import Brain
from loguru import logger

class Bot:
    ALIAS = 'UnkownBot'

    def __init__(self, brain: Brain):
        self.set_properties(brain)

    @classmethod
    def set_properties(cls, brain: Brain):
        """
        To-do: Figure out how best to deal with property inheritance
        - @property does not seems to assign inherited properties?
        """
        cls.brain = brain

    @classmethod
    def alias(cls):
        return cls.ALIAS

    @classmethod
    def ask(cls, question: str):
        return cls.brain().answer(question)
