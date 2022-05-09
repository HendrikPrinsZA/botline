import os
import random
from time import sleep

class Brain(object):
    ALIAS = 'UnkownBrain'
    NO_ANSWER = 'has no answer'
        
    @classmethod
    def alias(cls) -> str:
        return cls.ALIAS
    
    @classmethod
    def answer(cls, question: str) -> str:
        return cls.no_answer()
    
    @classmethod
    def no_answer(cls) -> str:
        return cls.NO_ANSWER

    @classmethod
    def answer_like_bot(self, alias: str, text: str):
        print(f"{alias}:", end = '')
        words = list(text.split(' '))
        for idx, word in enumerate(words):
            for char in word:
                print(char, end = '', flush = True)
                sleep(random.uniform(0.01, 0.1) * self.DELAY_CHAR)

            if idx < len(words) - 1:
                sleep(random.uniform(0.1, 0.5) * self.DELAY_WORD)
                print(' ', end = '', flush = True)
            else:
                print('')

    @classmethod
    def print_like_bot(self, text: str) -> str:
        """
        Print the text like a bot
        
        1. clear the screen
        2. show the prompt
        3. show the last answer like a bot
        4. return the next line (Human: )
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        lines = text.splitlines()
        prompt = lines.pop()
        bot_line = lines.pop()
        bot_parts = bot_line.split(':')
        print("\n".join(lines))
        self.answer_like_bot(bot_parts[0], bot_parts[1])
        return prompt