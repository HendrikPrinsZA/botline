import logging

from call_a_bot.bots.davinci import Davinci
from call_a_bot.brains.openai import OpenAi

def BrainFactory(brain: str = 'openai'):
    brain = brain.lower()
    brains = {
        'openai': OpenAi
    }
    
    try:
        brain_class = brains[brain]
    except:
        logging.error(f"Could not find brain for '{brain}'")
        exit(1)
        
    return brain_class()

def BotFactory(bot: str = 'Davinci', brain: str = 'openai'):
    bot = bot.lower()
    bots = {
        'davinci': Davinci
    }
    
    try:
        bot_class = bots[bot]
    except:
        logging.error(f"Could not find bot for '{bot}'")
        exit(1)
        
    brian = BrainFactory(brain)
    return bot_class(brian)