from call_a_bot.bots.bot import Bot
from call_a_bot.brains.brain import Brain
from call_a_bot.brains.terminal import Terminal

class Human(Bot):
    ALIAS = 'Human'

    def __init__(self, brain: Brain = Terminal()) -> None:
        super().__init__(brain)
