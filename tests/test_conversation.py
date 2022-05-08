import unittest

from botline.conversation import Conversation

class TestConversation(unittest.TestCase):
    MAX_MS = 3000

    def __init__(self, methodName):
        super().__init__(methodName)
        
    def test_basic(self):
        convo = Conversation('Sample bio')
        convo.append('Human', 'Hallo Bot')
        convo.append('Bot', 'Hallo Human')
        
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot')
        
        self.assertMultiLineEqual(
            """Sample bio

Human: Hallo Bot
Bot: Hallo Human
Human: What is 2 + 2?
Bot: """,
            convo.get_prompt()
        )
        
    def test_set_answer(self):
        convo = Conversation()
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot')
        convo.set_answer('4')
        self.assertMultiLineEqual(
            """Human: What is 2 + 2?
Bot: 4""",
            convo.get_prompt()
        )
        
    def test_undo(self):
        convo = Conversation()
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot', '4')
        convo.undo()
        self.assertMultiLineEqual(
            """Human: What is 2 + 2?
Bot: """,
            convo.get_prompt()
        )
        convo.undo()
        self.assertEqual('Human: ', convo.get_prompt())
        convo.undo()
        self.assertEqual(
            'Human: ', 
            convo.get_prompt(), 
            'Should not be able to undo any further!'
        )

if __name__ == '__main__':
    unittest.main()
