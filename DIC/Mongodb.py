from pymongo import MongoClient

database_ip = "localhost"
database_db = "test"

class MongoDB:
    def __init__(self):
        self.client = MongoClient(database_ip, 27017)

    def insert_into_graph(self, parent_url, childrens):
        collection = self.client[database_db]["WikiGraph"]
        data = {
            "parent_url": parent_url,
            "children": childrens
        }
        collection.insert_one(data)

    def is_url_processed(self, url):
        collection = self.client[database_db]["visitedNode"]
        document = collection.find_one({"url": url})
        if document:
            return True
        else:
            return False


    def add_url_status(self, url, status):
        collection = self.client[database_db]["visitedNode"]
        collection.insert_one({"url": url, "status": status})