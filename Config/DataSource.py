from pymongo import MongoClient

class DataSource:
    def __init__(self):
        self.hostname='localhost'
        self.port=27017
        self.dbtype='mongodb'
        self.defaultDB = 'ml_fuel'

    def getConnection(self):
        Connection = None
        if(self.dbtype=='mongodb'):
            Connection = MongoClient(self.hostname,self.port)
        
        self.Connection=Connection

    def getDB(self):
        self.getConnection()
        db = self.Connection[self.defaultDB]

        return db

    def close(self):
        self.Connection.close()

    



            





    