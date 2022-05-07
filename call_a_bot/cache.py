from datetime import datetime
import hashlib
import json
from os import path
from loguru import logger

class Cache:
    AUDIT_FIELDS = [
        'created_at', 'updated_at', 'viewed_at'
    ]

    def __init__(self, filepath):
        self.filepath = filepath
        self.set('viewed_at', datetime.now().timestamp())

    def hash(self, key):
        if key in self.AUDIT_FIELDS:
            return key

        return hashlib.md5(key.encode()).hexdigest()

    def get(self, key):
        hash = self.hash(key)

        value = None
        with open(self.filepath) as file_object:
            cache = json.load(file_object)
            try:
                value = self.decode(cache[hash])
            except:
                return None

        if key in self.AUDIT_FIELDS:
            if value is not None:
                return datetime.fromtimestamp(value)

        return value

    def set(self, key, value):
        created = False

        if not path.isfile(self.filepath):
            created = True
            self.clear()

        with open(self.filepath) as file_object:
            cache = json.load(file_object)
            file_object.close()

        hash = self.hash(key)
        with open(self.filepath, "w") as file_object:
            cache[hash] = self.encode(value)

            timestamp = datetime.now().timestamp()
            if created:
                cache['created_at'] = self.encode(timestamp)
            else:
                cache['updated_at'] = self.encode(timestamp)

            json.dump(cache, file_object)

        return value
    
    def clear(self):
        with open(self.filepath, 'w') as file_object:
            json.dump({
                'created_at': self.encode(datetime.now().timestamp())
            }, file_object)

    def decode(self, value):
        return json.loads(value)

    def encode(self, value):
        return json.dumps(value)