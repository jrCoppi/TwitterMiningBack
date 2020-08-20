import mysql.connector as mysql

class Base():
    db = ''

    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        self.db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "TwitterMining"
        )
    
    def insertData(self,query,values):
        cursor = self.db.cursor()
        cursor.execute(query, values)
        self.db.commit()
        return cursor.lastrowid

    def selectData(self,query):
        cursor = self.db.cursor()
        cursor.execute(query)
        return cursor.fetchall()