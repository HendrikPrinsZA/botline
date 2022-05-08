"""Enables use of Python CallABot as a "main" function (i.e. "python -m call_a_bot").

This allows using CallABot with third-party libraries without modifying their code.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from dotenv import load_dotenv
from loguru import logger
import os
import fire
from call_a_bot.core import CallABot

from call_a_bot.factories import BotFactory

PATH_ENV = os.path.abspath(f"{os.path.dirname(__file__)}/../.env")
load_dotenv(PATH_ENV)

import call_a_bot

cli_string = """usage: python -m call_a_bot"

Python CallABot is a library for communicating with AI bots
"""

class Main:
    """Python CallABot CLI"""
    
    def __init__(self) -> None:
        self.callabot = CallABot()
        
    def call(self) -> None:
        self.callabot.call()
  
if __name__ == '__main__':
    fire.Fire(Main)