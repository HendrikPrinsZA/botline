from botline.bots.bot import Bot
from botline.bots.davinci import Davinci
from botline.bots.fastgptj import FastGptJ
from botline.bots.human import Human
from botline.brains.nlpcloud import NlpCloud
from botline.brains.openai import OpenAi
from botline.brains.terminal import Terminal

def BrainFactory(brain: str = 'openai'):
    brain = brain.lower()
    brains = {
        'openai': OpenAi,
        'nlpcloud': NlpCloud,
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
        'fastgptj': FastGptJ,
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