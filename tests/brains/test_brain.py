import unittest
from call_a_bot.brains.brain import Brain

class TestOpenAi(unittest.TestCase):
    def test_create(self):
        brain = Brain()
        self.assertEqual('UnkownBrain', brain.alias())
        self.assertEqual(Brain.ALIAS, brain.alias())
        
    def test_answer(self):
        brain = Brain()
        answer = brain.answer('What is your favourite colour?')
        self.assertEqual(answer, brain.NO_ANSWER)
        
if __name__ == '__main__':
    unittest.main()