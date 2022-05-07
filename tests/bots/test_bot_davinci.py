from datetime import datetime
from os import path
import unittest

from call_a_bot.bots.bot_davinci import BotDavinci

class TestBotDavinci(unittest.TestCase):
  def __init__(self, methodName: str):
    super().__init__(methodName)

  def test_create(self):
    bot = BotDavinci()
    self.assertEqual('Davinci', bot.alias())
    
if __name__ == '__main__':
  unittest.main()