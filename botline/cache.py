from datetime import datetime
import hashlib
import json
import os
from typing import Any

class Cache(object):
    AUDIT_FIELDS = [
        'created_at', 'updated_at', 'viewed_at'
    ]

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

        dirname = os.path.dirname(self.filepath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        
        self.set('viewed_at', datetime.now().timestamp())

    def hash(self, key: str) -> str:
        if key in self.AUDIT_FIELDS:
            return key

        return hashlib.md5(key.encode()).hexdigest()

    def file_to_json(self, filepath: str) -> dict:
        try:
            with open(filepath) as file_object:
                cache = json.load(file_object)
                return dict(cache)
        except:
            print(f"Error: Unable to convert file to json at {filepath}")
            exit(1)


    def get(self, key: str) -> Any:
        hash = self.hash(key)

        if not os.path.isfile(self.filepath):
            return None

        cache = self.file_to_json(self.filepath)
        value = cache.get(hash, None)

        if value is None:
            return None

        if key in self.AUDIT_FIELDS:
            return datetime.fromtimestamp(float(value))

        try:
            return self.decode(value)
        except:
            print(f"Warning: Unable to decode corrupt value of {value}")
            return None

    def set(self, key: str, value: Any) -> Any:
        created = False

        if not os.path.isfile(self.filepath):
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
    
    def clear(self) -> None:
        with open(self.filepath, 'w') as file_object:
            json.dump({
                'created_at': self.encode(datetime.now().timestamp())
            }, file_object)

    def decode(self, value: str) -> Any:
        return json.loads(value)

    def encode(self, value: Any) -> str:
        return json.dumps(value)
