"""Enables use of Python BotLine as a "main" function (i.e. "python -m botline").

This allows using BotLine with third-party libraries without modifying their code.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from dotenv import load_dotenv
from loguru import logger
import os
import fire
from botline.core import BotLine

from botline.factories import BotFactory

PATH_ENV = os.path.abspath(f"{os.path.dirname(__file__)}/../.env")
load_dotenv(PATH_ENV)

import botline

cli_string = """usage: python -m botline"

Python BotLine is a library for communicating with AI bots
"""

class Main:
    """Python BotLine CLI"""
    
    def __init__(self) -> None:
        self.botline = BotLine()
        
    def call(self) -> None:
        self.botline.call()
  
if __name__ == '__main__':
    fire.Fire(Main)