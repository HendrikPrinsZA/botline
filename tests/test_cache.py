import os
import unittest
from datetime import datetime
from os import path

from call_a_bot.cache import Cache

class TestCacheMethods(unittest.TestCase):
    MAX_MS = 1500
    PATH_DIR = path.abspath(f"{path.dirname(__file__)}/../tests/__pycache__")
    PATH_CACHE = f"{PATH_DIR}/test_cache.json"

    def _clean(self):
        if path.isfile(self.PATH_CACHE):
            os.remove(self.PATH_CACHE)

    def __del__(self):
        self._clean()

    def __init__(self, methodName):
        super().__init__(methodName)

    def test_create(self):
        self.cache = Cache(self.PATH_CACHE)
        started_at = datetime.now()
        created_at = self.cache.get('created_at')
        
        difference = started_at - created_at
        self.assertLess(
            difference.microseconds, 
            self.MAX_MS, 
            f"Took longer than {self.MAX_MS} to save, check the algorithm!"
        )
        self.assertIsInstance(created_at, datetime)    

if __name__ == '__main__':
    unittest.main()
