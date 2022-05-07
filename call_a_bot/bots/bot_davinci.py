
from call_a_bot.bots.bot import Bot

class BotDavinci(Bot):
  ALIAS = 'Davinci'

  def __init__(self):
    super().__init__()
    print('BotDavinci.__init__')

  
