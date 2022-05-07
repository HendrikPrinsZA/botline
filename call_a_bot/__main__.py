from cache import Cache
from os import path

PATH_CACHE = path.abspath(f"{path.dirname(__file__)}/../.cache.json")

cache = Cache(PATH_CACHE)

def main():
  print('hallo from main()')