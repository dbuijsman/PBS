from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class Database:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://stockService:AxwY0SbZ8hVNzIUI@pbs.gv3zv.mongodb.net/PBS?retryWrites=true&w=majority")
        try:
            self.client.admin.command('ismaster')
        except ConnectionFailure:
            print("Server not available")
