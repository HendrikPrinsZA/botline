import unittest

from call_a_bot.conversation import Conversation

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
        
    def test_set_last_message_text(self):
        convo = Conversation()
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot')
        convo.set_last_message_text('4')
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
            'Human: What is 2 + 2?',
            convo.get_prompt()
        )
    
    def test_redo(self):
        convo = Conversation()
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot', '4')
        convo.undo()
        convo.redo()
        convo.undo()
        convo.redo()
        self.assertMultiLineEqual(
            """Human: What is 2 + 2?
Bot: 4""",
            convo.get_prompt()
        )

if __name__ == '__main__':
    unittest.main()
