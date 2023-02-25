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
            UNIQUE (contact)
            UNIQUE (instagram)
);"""
#cursor.execute(table)

class DataModel:
    def __init__(self,name):
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT id,name,contact,instagram,confirmation,count,cost FROM information where name = ?",[name])
        output = cursor.fetchall()
        self.name_exist = True
        if(bool(output) == False):
            self.name_exist = False
        else: 
            result = output[0]
            self.information = {}
            self.information['id'] = result[0]
            self.information['name'] = result[1]
            self.information['contact'] = result[2]
            self.information['instagram'] = result[3]
            self.information['confirmation'] = result[4]
            self.information['count'] = result[5]
            self.information['cost'] = result[6]

    def copy_attributes(self,dictionary):
        self.information = dictionary

    def __repr__(self):
        output = f" ID : {self.id} \n name : {self.name} \n contact : {self.contact} \n instagram : {self.instagram} \n confirmation : {self.confirmation} \n cost : {self.cost}"
        return output

    @staticmethod
    def check_duplicate(name):
        cursor = sqliteConnection.cursor()
        query = """SELECT id,name,contact,confirmation,count,cost FROM information where name = ?"""
        cursor.execute(query,[name])
        results = cursor.fetchall()
        if name in results[0]:
            table = tabulate(results, headers = ["id","name","contact","confirmation","count","cost"])
            return True,table,results
        else:
            return False

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
    def model_delete_using_ID_DB(name,id):
        cursor = sqliteConnection.cursor()
        query = """SELECT id,name FROM information where id = ?"""
        cursor.execute(query,[id])
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
        cursor.execute("""SELECT name,contact,confirmation,count,cost,instagram FROM information""") #where id IN (%s)"""%("?," * len(rows))[:-1], rows
        result = cursor.fetchall()
        return result

    @staticmethod
    def model_show_one_DB(name):
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT name,contact,confirmation,count,cost,instagram FROM information where name = ?",[name])
        result = cursor.fetchall()
        return result[0]

    def model_update_DB(self):
        cursor = sqliteConnection.cursor()
        params = (self.information['name'],self.information['contact'],self.information['instagram'],self.information['confirmation'],int(self.information['count']),int(self.information['cost']),int(self.information['id']))
        query = f"""UPDATE information 
                    SET name = ?,
                        contact= ?,
                        instagram = ?,
                        confirmation = ?,
                        count = ?,
                        cost = ?
                    WHERE id = ?;
                    """
        cursor.execute(query,params)
        sqliteConnection.commit()
        return "updated" 


