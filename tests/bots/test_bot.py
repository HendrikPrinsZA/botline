import unittest
from call_a_bot.bots.bot import Bot
from call_a_bot.brains.brain import Brain
from call_a_bot.brains.openai import OpenAi

class TestBot(unittest.TestCase):
    def test_create_generic(self):
        brain = Brain()
        bot = Bot(brain)
        self.assertEqual(Bot.ALIAS, bot.alias())
        self.assertEqual(Brain.ALIAS, bot.brain.alias())
    
    def test_create_openai(self):
        brain = OpenAi()
        bot = Bot(brain)
        self.assertEqual(Bot.ALIAS, bot.alias())
        self.assertEqual(OpenAi.ALIAS, bot.brain.alias())
        
if __name__ == '__main__':
    unittest.main()