import pymongo

class Database:
    def __init__(self):    
        self.client = pymongo.MongoClient('mongodb://localhost/')
        self.mydb = client['Employee']
        self.info = mydb.employeeinformation
        