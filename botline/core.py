from loguru import logger
from botline.conversation import Conversation
from botline.factories import BotFactory

class BotLine(object):
    def __init__(self) -> None:
        self.human = BotFactory('Human')
        self.bot = BotFactory('Davinci')

        self.convo = Conversation(self.human, self.bot)

    def call(self) -> None:
        self.convo.append(self.human.ALIAS)
        answer = self.human.ask(self.convo.get_prompt())

        if answer.startswith('.'):
            self.command(answer)
            return
        else:
            self.convo.set_answer(answer)
        
        self.convo.append(self.bot.ALIAS)
        answer = self.bot.ask(self.convo.get_prompt())
        self.convo.set_answer(answer)

        self.call()
    
    def command(self, answer: str) -> None:
        if answer == '.exit':
            exit() 

        if answer == '.undo':
            self.convo.undo(2)
            self.call()
            return
        
        logger.error(f"Command '{answer}' not found")
        self.call()
