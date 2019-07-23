# -*- coding:utf-8 -*-
import datetime
import json
import redis
import base.settings as settings



class BaseRedis(object):
    redis_host = settings.REDIS_CONFIG['host']
    redis_port = settings.REDIS_CONFIG['port']
    redis_db = 1
    redis_password = settings.REDIS_CONFIG['password']

    def __init__(self):
        self.r = redis.Redis(host=self.redis_host, port=self.redis_port, db=self.redis_db, password=self.redis_password)

    def set(self, key, value):
        return self.r.set(key, value)

    # 设置 key 对应的值为 string 类型的 value。如果 key 已经存在,返回 0,nx 是 not exist 的意思
    def setnx(self, key, value):
        return self.r.setnx(key, value)

    def hset(self, name, key, content):
        return self.r.hset(name=name, key=key, value=content)

    def delete(self, key):
        return self.r.delete(key)

    def hdel(self, name, key=None):
        if (key):
            return self.r.hdel(name, key)
        return self.r.hdel(name)

    def hget(self, name, key):
        return self.r.hget(name, key)

    def get(self, name):
        return self.r.get(name)

    def srem(self, name, value):
        return self.r.srem(name, value)

    def zadd(self, name, args, kwargs):
        self.r.zadd(name, args, kwargs)
