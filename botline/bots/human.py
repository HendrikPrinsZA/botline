from botline.bots.bot import Bot
from botline.brains.brain import Brain
from botline.brains.terminal import Terminal

class Human(Bot):
    ALIAS = 'Human'

    def __init__(self, brain: Brain = Terminal()) -> None:
        super().__init__(brain)
