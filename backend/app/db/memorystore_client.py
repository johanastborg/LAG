import redis
import os

class MemoryStoreClient:
    def __init__(self, host, port=6379):
        self.client = redis.Redis(host=host, port=port)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, ttl=3600):
        return self.client.set(key, value, ex=ttl)
