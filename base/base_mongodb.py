# -*- coding:utf-8 -*-

from pymongo import MongoClient


class MongoApi:
    def __init__(self, database=None):
        self.client = MongoClient(host="172.19.0.213", port=27217, username='admin', password='admin')
        self.database = database

    def get_db(self):
        """
        建立连接进行认证，返回数据库
        """
        # 建立连接
        db = self.client[self.database]
        return db

    def insert_doc(self, coll, doc):
        """
        mongo中插入数据
        """
        db = self.get_db()
        coll = db[coll]
        res = coll.insert(doc)
        return res

    def get_doc(self, db, collection, doc):
        """
        mongo中读取数据，省略_id字段
        """
        coll = db[collection]
        res = coll.find(doc, {"_id": 0})
        return res

    def filter_all(self, coll):
        """
        mongo中读取数据
        """
        lists = []
        db = self.get_db()
        coll = db[coll]
        for i in coll.find():
            lists.append(i)
        return lists

    def filter_only_one(self, coll, data):
        """
        根据mongo_id 查询数据
        data传入{}
        """
        db = self.get_db()
        coll = db[coll]
        return coll.find_one(data)

    def return_count(self, coll):
        db = self.get_db()
        coll = db[coll]
        print(coll.find({"object_uid": {"$exists": True}}).count())

    def delete_all(self, coll, data):
        db = self.get_db()
        coll = db[coll]
        # 删除data的全部记录
        coll.remove(data)

    def delete_only_one(self, coll, data):
        # 删除name=li的某个id的记录
        db = self.get_db()
        coll = db[coll]
        delete_id = coll.find_one(data)['_id']
        coll.remove(delete_id)

    def update_doc(self, coll, data1, data2):
        db = self.get_db()
        coll = db[coll]
        coll.update(data1, {'$set': data2})