import unittest

from call_a_bot.bots.davinci import Davinci

class TestDavinci(unittest.TestCase):
    def test_create(self):
        bot = Davinci()
        self.assertEqual('Davinci', bot.alias())
        
    def test_ask(self):
        bot = Davinci()
        answer = bot.ask('What is your favourite colour?')
        self.assertEqual(answer, 'I don\'t know')
        
if __name__ == '__main__':
    unittest.main()