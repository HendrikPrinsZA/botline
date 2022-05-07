from call_a_bot.bots.bot import Bot
from call_a_bot.brains.brain import Brain
from call_a_bot.brains.openai import OpenAi

class Davinci(Bot):
    ALIAS = 'Davinci'

    def __init__(self, brain: Brain = OpenAi):
        super().__init__(brain)

