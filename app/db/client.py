import os
from pymongo import MongoClient, DESCENDING as DESC, ASCENDING as ASC
from bson.objectid import ObjectId


def with_connection(func):
    def with_connection_(self, *args, **kwargs):
        global db
        mongo_host = os.environ.get('MONGO_HOST')
        mongo_port = 27017 if os.environ.get('MONGO_PORT') is None else int(os.environ.get('MONGO_PORT'))
        client = MongoClient(host=mongo_host, port=mongo_port)
        db = client.document_database
        try:
            wrapper = func(self, db, *args, **kwargs)
            print('Query successfuly performed')
        except Exception:
            raise Exception('Query failure')
        finally:
            client.close()
            db = None
            print('Connection successfuly closed')
        return wrapper
    return with_connection_

class Database:
    def __init__(self):
        if not os.environ.get('MONGO_HOST'):
            raise Exception('You should define MONGO_HOST environment variable')

    @with_connection
    def insert(self, db, data):
        entry_id = db.apple_collection.insert_one(data)
        return entry_id

    @with_connection
    def increment(self,db, entry_id, value):
        db.apple_collection.update_one({'_id': ObjectId(entry_id)}, {"$inc": {'mentions': value, 'search_count': 1} })

    @with_connection
    def all(self, db):
        return db.apple_collection.find({}).sort([("mentions", DESC),
                                                  ("count", DESC),
                                                  ("name", ASC)])
