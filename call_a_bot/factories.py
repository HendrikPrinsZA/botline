from call_a_bot.bots.bot import Bot
from call_a_bot.bots.davinci import Davinci
from call_a_bot.bots.human import Human
from call_a_bot.brains.openai import OpenAi
from call_a_bot.brains.terminal import Terminal

def BrainFactory(brain: str = 'openai'):
    brain = brain.lower()
    brains = {
        'openai': OpenAi,
        'terminal': Terminal
    }
    
    try:
        brain_class = brains[brain]
    except:
        return None
        
    return brain_class()

def BotFactory(bot: str = 'Davinci', brain: str = None) -> Bot:
    bot = bot.lower()
    bots = {
        'davinci': Davinci,
        'human': Human
    }
    
    try:
        bot_class = bots[bot]
    except:
        return None
        
    if brain is not None:
        brian = BrainFactory(brain)
        return bot_class(brian)

    return bot_class()