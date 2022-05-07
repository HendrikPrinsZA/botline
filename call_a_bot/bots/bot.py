from loguru import logger

from call_a_bot.brains.brain import Brain

class Bot:
  ALIAS = 'UnkownBot'

  def __init__(self, brain: Brain):
    self.setProperties(brain)
    
  @classmethod
  def setProperties(self, brain: Brain):
    # To-do: Figure out how best to deal with property inheritance
    # - @property does not seems to assign inherited properties?
    self.brain = brain

  @classmethod
  def alias(self):
    return self.ALIAS

  @classmethod
  def ask(self, question: str):
    if self.brain: 
      return self.brain().answer(question)
    
    # return "I can't think without a brain"
    raise Exception("I can't think without a brain!")
      
    
