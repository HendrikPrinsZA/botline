
from datetime import datetime

from call_a_bot.bots.bot import Bot

class Message:
    def __init__(self, alias, text = None):
        self.alias = alias
        self.datetime = datetime.now()
        self._text = text
    
    def __str__(self):
        line = line = f"{self.alias}: "
        
        if self.text is not None:
            line = f"{line}{self.text}"
            
        return line
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text: str):
        text = text.strip()
        self._text = text

class Conversation:
    
    def __init__(self, bio: str = ''):
        self.history = []
        self.messages = []
        self.bio = bio
        
    def append(self, alias, text = None):
        message = Message(alias, text)
        self.messages.append(message)
        self._save_history()

    def set_last_message_text(self, text: str):
        last_message = self.messages[-1]
        last_message.text = text
        self._save_history()
        
    def undo(self, count: int = 1):
        pos = (count + 1) * -1
        
        if len(self.history) > count:
            self.messages = self.history[pos].copy()
            self._save_history()
            
    def redo(self, count: int = 1):
        self.undo(count)
        
    def get_prompt(self):
        lines = []
        
        if len(self.bio) > 0:
            lines.append(self.bio.strip())
            lines.append('')
        
        for message in self.messages:
            lines.append(str(message))
            
        return "\n".join(lines)
    
    def _save_history(self):
        self.history.append(self.messages.copy())
        