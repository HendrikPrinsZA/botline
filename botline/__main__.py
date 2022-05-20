"""Enables use of Python BotLine as a "main" function (i.e. "python -m botline").

This allows using BotLine with third-party libraries without modifying their code.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import fire

from botline.core import BotLine

cli_string = """usage: python -m botline"

Python BotLine is a library for communicating with AI bots
"""

class Main(object):
    """Python BotLine CLI"""
    
    def __init__(self) -> None:
        self.botline = BotLine()
        
    def call(self) -> None:
        self.botline.call()
  
if __name__ == '__main__':
    fire.Fire(Main)