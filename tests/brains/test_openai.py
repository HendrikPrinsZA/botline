import unittest

from call_a_bot.brains.openai import OpenAi

# from call_a_bot.bots.davinci import Davinci

class TestOpenAi(unittest.TestCase):
    def test_create(self):
        brain = OpenAi()
        self.assertEqual('OpenAI', brain.alias())
        self.assertEqual(OpenAi.ALIAS, brain.alias())
        
    def test_answer(self):
        brain = OpenAi()
        
        answer = brain.answer('What is your favourite colour?')
        self.assertEqual(answer, "I don't have an answer")
        
if __name__ == '__main__':
    unittest.main()