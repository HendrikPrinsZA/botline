class Bot:
  NAME = 'Unkown'

  def __init__(self):
    print('BotDavinci.__init__')
    self.alias_human = "Human:"
    self.alias_bot = "Davinci:"

  @classmethod
  def alias(self):
    return self.ALIAS
