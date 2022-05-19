import unittest

from botline.bots.bot import Bot
from botline.conversation import Conversation
from botline.factories import BotFactory

class TestConversation(unittest.TestCase):
    maxDiff = None

    def __init__(self, methodName):
        super().__init__(methodName)
        self.convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        self.convo_base = self.convo.get_text()
        
    def test_basic(self):
        self.convo.append('Human', 'Hallo Bot')
        self.convo.append('Bot', 'Hallo Human')
        
        self.convo.append('Human', 'What is 2 + 2?')
        self.convo.append('Bot')

        self.assertMultiLineEqual(
            f"""{self.convo_base}
Human: Hallo Bot
Bot: Hallo Human
Human: What is 2 + 2?
Bot: """,
            self.convo.get_text()
        )
        
    def test_set_answer(self):
        convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        self.convo.append('Human', 'What is 2 + 2?')
        self.convo.append('Bot')
        self.convo.set_answer('4')
        self.assertMultiLineEqual(
            f"""{self.convo_base}
Human: What is 2 + 2?
Bot: 4""",
            self.convo.get_text()
        )
        
    def test_undo(self):
        convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        self.convo.append('Human', 'What is 2 + 2?')
        self.convo.append('Bot', '4')
        self.convo.undo()
        self.assertMultiLineEqual(
            f"""{self.convo_base}
Human: What is 2 + 2?
Bot: """,
            self.convo.get_text()
        )
        self.convo.undo()
        self.assertMultiLineEqual(
            f"""{self.convo_base}
Human: """,
            self.convo.get_text()
        )

        self.convo.undo(1000)
        self.assertMultiLineEqual(
            f"""I'm Davinci, the most capable GPT-3 model, also known as text-davinci-002. I can do any task the other models can do, often with less context. In addition to responding to prompts, also supports inserting completions within text.

Human: """,
            self.convo.get_text()
        )

if __name__ == '__main__':
    unittest.main()
