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


#class initialized with a connection to the database 
class DataModel:         


    #constructor -> takes name as input, fetches all the related information if the name exists in database               
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


    # checks for duplicate instances , takes a name as input. Returns True if duplicates present
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


    # deletes a row from the database, takes name as input. Returns a message based on the success of deletion
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


    # deletes a row from the database using ID. Takes name and id as input. Returns a message based on the success of deletion
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


    # inserts a row into the database using parameters. Takes different parameters as input. Returns a message when inserted
    @staticmethod
    def model_insert_DB(name,contact,instagram,confirmation,count,cost):
        cursor = sqliteConnection.cursor()
        query = """INSERT INTO information(name,contact,instagram,confirmation,count,cost) VALUES (?,?,?,?,?,?) """
        cursor.execute(query,(name,contact,instagram,confirmation,count,cost))
        sqliteConnection.commit()
        return f"{name} inserted successfully"
        #add validation that its inserted successfully        
    

    # accesses database and grabs all columns and rows and returns a list of tuples as output.
    @staticmethod
    def model_show_all_DB():
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT COUNT(name) FROM information")
        cursor.execute("""SELECT name,contact,confirmation,count,cost,instagram FROM information""") #where id IN (%s)"""%("?," * len(rows))[:-1], rows
        result = cursor.fetchall()
        return result


    # grabs the row by name and outputs the full row. Returns a tuple with user information.
    @staticmethod
    def model_show_one_DB(name):
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT name,contact,confirmation,count,cost,instagram FROM information where name = ?",[name])
        result = cursor.fetchall()
        return result[0]


    # grabs class attributes (dictionary named information) and pushes the updates into the Database. 
    # Returns an output message when updated.
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

    @staticmethod
    def model_show_total_cost():
        cursor = sqliteConnection.cursor()
        query = """SELECT cost FROM information;"""
        cursor.execute(query)
        results = cursor.fetchall()
        cost = []
        for integer in results:
            cost.append(integer[0])
        total_cost = sum(cost)
        return total_cost



