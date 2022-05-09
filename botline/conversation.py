
from datetime import datetime

from botline.bots.bot import Bot

class Message(object):
    def __init__(self, alias: str, text: str = None) -> None:
        self.alias = alias
        self.datetime = datetime.now()
        self._text = text
    
    def __str__(self) -> str:
        line = line = f"{self.alias}: "
        
        if self.text is not None:
            line = f"{line}{self.text}"
            
        return line
    
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, text: str) -> None:
        if text is not None:
            text = text.strip()
        self._text = text

class Conversation:
    
    def __init__(self, human: Bot, bot: Bot) -> None:
        self.human = human
        self.bot = bot
        self.history = []
        self.messages = []
        self.bot_bio_messages()

    def bot_bio_messages(self) -> None:
        if self.bot.BIO_MESSAGES is None:
            return

        for message in self.bot.BIO_MESSAGES:
            self.append(self.human.ALIAS, message['question'])
            self.append(self.bot.ALIAS, message['answer'])
        
    def append(self, alias: str, text: str = None) -> None:
        message = Message(alias)
        self.messages.append(message)
        if text is not None:
            self.set_answer(text)

    def set_answer(self, text: str) -> None:
        self.messages[-1].text = text
        self._save_history()
        
    def undo(self, count: int = 1) -> None:
        if count > len(self.history):
            count = len(self.history) - 1

        pos = (count + 1) * -1
        last_message = self.messages[-1]
        if last_message.text is not None:
            last_message.text = None
        elif len(self.history) > count:
            self.messages = self.history[pos].copy()
            self.messages[-1].text = None
        
    def get_text(self) -> str:
        lines = []
        
        if len(self.bot.BIO) > 0:
            bio = ""
            for line in self.bot.BIO.splitlines():
                line = line.strip()
                bio = f"{bio} {line}"

            lines.append(bio.strip())
            lines.append('')
        
        for message in self.messages:
            lines.append(str(message))
            
        return "\n".join(lines)
    
    def _save_history(self) -> None:
        self.history.append(self.messages.copy())
        