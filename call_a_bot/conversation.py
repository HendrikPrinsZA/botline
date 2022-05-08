
from datetime import datetime

from call_a_bot.bots.bot import Bot

class Message:
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
    
    def __init__(self, bio: str = '') -> None:
        self.history = []
        self.messages = []
        self.bio = bio
        
    def append(self, alias: str, text: str = None) -> None:
        message = Message(alias, text)
        self.messages.append(message)
        self._save_history()

    def set_answer(self, text: str) -> None:
        self.messages[-1].text = text
        self._save_history()
        
    def undo(self, count: int = 1) -> None:
        pos = count + 1 * -1
        
        last_message = self.messages[-1]
        if last_message.text is not None:
            last_message.text = None
        elif len(self.history) > count:
            self.messages = self.history[pos].copy()
            self.messages[-1].text = None
        
    def get_prompt(self) -> str:
        lines = []
        
        if len(self.bio) > 0:
            lines.append(self.bio.strip())
            lines.append('')
        
        for message in self.messages:
            lines.append(str(message))
            
        return "\n".join(lines)
    
    def _save_history(self) -> None:
        self.history.append(self.messages.copy())
        