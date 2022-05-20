from botline.bots.bot import Bot
from botline.brains.brain import Brain
from botline.brains.nlpcloud import NlpCloud

class FastGptJ(Bot):
    ALIAS = 'FastGptJ'

    BIO_MESSAGES = [
        {
            "question": "Who are you?",
            "answer": "I'm GPT-J, an open-source Natural Language Processing model created by EleutherAI"
        }
    ]

    def __init__(self, brain: Brain = NlpCloud()) -> None:
        super().__init__(brain)

