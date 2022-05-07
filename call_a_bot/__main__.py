from cache import Cache
from os import path

from call_a_bot.bots.davinci import Davinci

PATH_ENV = path.abspath(f"{path.dirname(__file__)}/../.env")
PATH_CACHE = path.abspath(f"{path.dirname(__file__)}/../.cache.json")

bot = Davinci()

def main():
  print('hallo from main()')