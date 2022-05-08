from botline.bots.bot import Bot
from botline.brains.brain import Brain
from botline.brains.openai import OpenAi

class Davinci(Bot):
    ALIAS = 'Davinci'

    def __init__(self, brain: Brain = OpenAi()) -> None:
        super().__init__(brain)

