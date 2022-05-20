from botline.brains.brain import Brain

class Terminal(Brain):
    ALIAS = 'Terminal'
    NO_ANSWER = 'is not available'
    
    DELAY_WORD = 0.5
    DELAY_CHAR = 0.1

    def answer(self, text: str) -> str:
        prompt = self.print_like_bot(text)
        try:
            answer = input(prompt)
        except:
            exit()
        
        if len(answer) == 0:
            return self.answer(text)

        return answer