# model functions for the CRUD Application, the purpose of this script is only to access database not take user input.

#creating a database locally, if you want to implement this in your hardware just remove the # from the commented chunk of code
import sqlite3
from tabulate import tabulate
sqliteConnection = sqlite3.connect('party.db')
#cursor = sqliteConnection.cursor()
#print("database initialized")
#cursor.execute("DROP TABLE IF EXISTS information;")
table =  """CREATE TABLE information (
            id integer PRIMARY KEY,
            name TEXT DEFAULT None,
            contact TEXT DEFAULT None,
            instagram TEXT DEFAULT None,
            confirmation TEXT DEFAULT "no",
            count INTEGER DEFAULT 0,
            cost INTEGER DEFAULT 18,
            UNIQUE (name,contact,instagram)
);"""
#cursor.execute(table)

class DataModel:
    def __init__(self):
        self.id = None
        self.name = None
        self.contact = None
        self.instagram = None
        self.confirmation = None
        self.count = None
        self.cost= None

    def __repr__(self):
        information = []
        information.append(self.id)
        information.append(self.name)
        information.append(self.contact)
        information.append(self.instagram)
        information.append(self.confirmation)
        information.append(self.count)
        information.append(self.cost)
        return print(tabulate(information,headers=["name","contact","confirmation","count","cost","instagram"]))

    @staticmethod
    def model_delete_DB(name):
        cursor = sqliteConnection.cursor()
        query = """SELECT id,name FROM information """
        cursor.execute(query)
        result = cursor.fetchall()
        for tuple in result:
            if name in tuple:
                cursor.execute("DELETE FROM information WHERE id = ?",[int(tuple[0])])
                sqliteConnection.commit()
                return f"{name} deleted successfully"
            else :
                return f"{name} not found in database"

    @staticmethod
    def model_insert_DB(name,contact,instagram,confirmation,count,cost):
        cursor = sqliteConnection.cursor()
        query = """INSERT INTO information(name,contact,instagram,confirmation,count,cost) VALUES (?,?,?,?,?,?) """
        cursor.execute(query,(name,contact,instagram,confirmation,count,cost))
        sqliteConnection.commit()
        return f"{name} inserted successfully"
        #add validation that its inserted successfully        
    

    @staticmethod
    def model_show_all_DB():
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT COUNT(name) FROM information")
        rows  = tuple([i+1 for i in range(int(cursor.fetchall()[0][0]))])
        cursor.execute("""SELECT name,contact,confirmation,count,cost,instagram FROM information where id IN (%s)"""%("?," * len(rows))[:-1], rows)
        result = cursor.fetchall()
        return result

    @staticmethod
    def model_show_one_DB(name):
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT name,contact,confirmation,count,cost,instagram FROM information where name = ?",[name])
        result = cursor.fetchall()
        return result[0]