import unittest

from botline.bots.davinci import Davinci

class TestDavinci(unittest.TestCase):
    def test_create(self):
        bot = Davinci()
        self.assertEqual('Davinci', bot.alias())

    # To-do: Mock the API
    # def test_ask(self):
    #     bot = Davinci()
    #     answer = bot.ask('What is your favourite colour?')
    #     self.assertEqual(answer, bot.brain.NO_ANSWER)
        
if __name__ == '__main__':
    unittest.main()