import unittest

from botline.brains.openai import OpenAi

class TestOpenAi(unittest.TestCase):
    def test_create(self):
        brain = OpenAi()
        self.assertEqual('OpenAI', brain.alias())
        self.assertEqual(OpenAi.ALIAS, brain.alias())
        
    # To-do: Mock the API
    # def test_answer(self):
    #     brain = OpenAi()
    #     answer = brain.answer('What is your favourite colour?')
    #     self.assertEqual(answer, brain.NO_ANSWER)
        
if __name__ == '__main__':
    unittest.main()