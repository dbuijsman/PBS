from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.client = MongoClient("mongodb+srv://stockService:AxwY0SbZ8hVNzIUI@pbs.gv3zv.mongodb.net/PBS?retryWrites=true&w=majority")