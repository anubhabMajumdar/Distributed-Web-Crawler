from pymongo import MongoClient
from configFile import *


class MongoDb:
    def __init__(self):
        self.client = MongoClient(DATABASE_IP, DATABASE_PORT)

    def insert_into_graph(self, parent_url, children):
        collection = self.client[DATABASE_NAME][COLLECTION_GRAPH]
        data = {
            "parent_url": parent_url,
            "children": children
        }
        collection.insert_one(data)

    def is_url_processed(self, url):
        collection = self.client[DATABASE_NAME][COLLECTION_VISITED]
        document = collection.find_one({"url": url})
        if document:
            return True
        else:
            return False

    def add_url_status(self, url, status):
        collection = self.client[DATABASE_NAME][COLLECTION_GRAPH]
        document = collection.find_one({"url": url})
        if document:
            document["status"] = status
            collection.save(document)
        else:
            collection.insert_one({"url": url, "status": status})
