import config
from pymongo import MongoClient

client = MongoClient(host=config.MONGO_ENDPOINT,port=config.MONGO_PORT)
db = client[config.DB_NAME]


def insert(collection_name:str,object_to_insert:object):
    return db[collection_name].insert_one(object_to_insert)

