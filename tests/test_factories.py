import unittest
from call_a_bot.bots.davinci import Davinci
from call_a_bot.brains.openai import OpenAi
from call_a_bot.factories import BotFactory, BrainFactory

class TestFactories(unittest.TestCase):
    def test_create_default(self):
        bot = BotFactory()
        self.assertIsInstance(bot, Davinci)

    def test_create_all(self):
        types = {
            'davinci': [Davinci, OpenAi]
        }

        for type in types:
            bot = BotFactory(type)
            self.assertIsInstance(bot, types[type][0])
            self.assertIsInstance(bot.brain, types[type][1])

    def test_create_bot_exception(self):
        bot = BotFactory('DoesNotExist')
        self.assertIsNone(bot)

    def test_create_brain_exception(self):
        bot = BrainFactory('DoesNotExist')
        self.assertIsNone(bot)
        
if __name__ == '__main__':
    unittest.main()