import os
import random
import unittest
from datetime import datetime
from os import path

from call_a_bot.cache import Cache
class TestCacheMethods(unittest.TestCase):
    MAX_MS = 3000
    PATH_DIR = path.abspath(f"{path.dirname(__file__)}/../tests/__pycache__")
    PATH_CACHE = f"{PATH_DIR}/test_cache.json"

    def __init__(self, methodName):
        super().__init__(methodName)
        self.cache = Cache(self.PATH_CACHE)
        self.cache.clear()
        
    def test_create(self):
        started_at = datetime.now()
        created_at = self.cache.get('created_at')
        
        difference = started_at - created_at
        self.assertLess(
            difference.microseconds, 
            self.MAX_MS, 
            f"Took longer than {self.MAX_MS} to save, check the algorithm!"
        )
        self.assertIsInstance(created_at, datetime) 
    
    def test_hash(self):
        hash = self.cache.hash('Random Text')
        self.assertEqual('9da6b4dc0a1e0a6b0d740dc7c5bf1d4f', hash)
        
    def test_hash_audit_fields(self):
        field = random.choice(Cache.AUDIT_FIELDS)
        hash = self.cache.hash(field)
        self.assertEqual(field, hash)
        
    def test_set_and_get(self):
        self.cache.set('random_key', 'random_value')
        self.assertEqual('random_value', self.cache.get('random_key'))
    
    def test_get_fail(self):
        value = self.cache.get('random_key')
        self.assertIsNone(value)
        
    def test_clear(self):
        self.cache.set('random_key', 'random_value')
        self.cache.clear()
        self.assertIsNone(self.cache.get('random_key'))
    
    def test_set_not_exist(self):
        if path.isfile(self.PATH_CACHE):
            os.remove(self.PATH_CACHE)
            
        self.cache.set('random_key', 'random_value')
        self.assertEqual('random_value', self.cache.get('random_key'))

if __name__ == '__main__':
    unittest.main()
