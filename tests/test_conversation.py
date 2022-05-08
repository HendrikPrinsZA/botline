import unittest
from botline.bots.bot import Bot

from botline.conversation import Conversation
from botline.factories import BotFactory

class TestConversation(unittest.TestCase):
    MAX_MS = 3000
    
    DAVINCI_BASE = """I'm Davinci, the most capable GPT-3 model, also known as text-davinci-002. I can do any task the other models can do, often with less context. In addition to responding to prompts, also supports inserting completions within text.

Human: Who are you?
Davinci: I'm Davinci, the most capable GPT-3 model, also known as text-davinci-002
Human: What is Davinci?
Davinci: Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and creative content generation, Davinci is going to produce the best results. These increased capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other engines.
Human: What are you good at?
Davinci: Complex intent, cause and effect, summarization for audience
Human: Can you tell me anything else?
Davinci: Another area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect."""

    def __init__(self, methodName):
        super().__init__(methodName)
        
    def test_basic(self):
        convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        convo.append('Human', 'Hallo Bot')
        convo.append('Bot', 'Hallo Human')
        
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot')

        self.assertMultiLineEqual(
            f"""{self.DAVINCI_BASE}
Human: Hallo Bot
Bot: Hallo Human
Human: What is 2 + 2?
Bot: """,
            convo.get_prompt()
        )
        
    def test_set_answer(self):
        convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot')
        convo.set_answer('4')
        self.assertMultiLineEqual(
            f"""{self.DAVINCI_BASE}
Human: What is 2 + 2?
Bot: 4""",
            convo.get_prompt()
        )
        
    def test_undo(self):
        convo = Conversation(BotFactory('Human'), BotFactory('Davinci'))
        convo.append('Human', 'What is 2 + 2?')
        convo.append('Bot', '4')
        convo.undo()
        self.assertMultiLineEqual(
            f"""{self.DAVINCI_BASE}
Human: What is 2 + 2?
Bot: """,
            convo.get_prompt()
        )
        convo.undo()
        self.assertMultiLineEqual(
            f"""{self.DAVINCI_BASE}
Human: """,
            convo.get_prompt()
        )

        convo.undo(1000)
        self.assertMultiLineEqual(
            f"""I'm Davinci, the most capable GPT-3 model, also known as text-davinci-002. I can do any task the other models can do, often with less context. In addition to responding to prompts, also supports inserting completions within text.

Human: """,
            convo.get_prompt()
        )

if __name__ == '__main__':
    unittest.main()
