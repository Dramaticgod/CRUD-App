
import sqlite3
from tabulate import tabulate

"""This chunk of code is for creation of table , only implement this once. After the implementation, 
comment out the executables for cursor object. Feel free to change the column names in the table and throughout the code"""

sqliteConnection = sqlite3.connect('party.db')
cursor = sqliteConnection.cursor()
print("database initialized")
#cursor.execute("DROP TABLE IF EXISTS information;")
table =  """CREATE TABLE information (
            id integer PRIMARY KEY,
            name TEXT,
            contact TEXT DEFAULT None,
            instagram TEXT DEFAULT None,
            confirmation TEXT DEFAULT "no",
            count INTEGER DEFAULT 0,
            cost INTEGER DEFAULT 18,
            UNIQUE (name,contact,instagram)
);"""
#cursor.execute(table)
sqliteConnection.close()

def lookupDB(Name):
    sqlConnection = sqlite3.connect("party.db")
    cursor = sqlConnection.cursor()
    query = """SELECT id,name FROM information """
    cursor.execute(query)
    result = cursor.fetchall()
    for tuple in result:
        if Name in tuple:
            sqlConnection.close()
            return tuple[0],tuple[1],True  # returns the name and id of the person
    else :
        sqlConnection.close()
        return False

        
def insertDB():
    name_db = input("Name : ").lower()
    contact_db = input("Phone Number : ")
    instagram_db = input("Instagram : ")
    confirmation_db = input("Are they attending yes/no ?  :  ").lower()
    count_db = int(input("How many people including the person attending (0-3): "))
    cost_db = 18*count_db


    sqlConnection = sqlite3.connect("party.db")
    cursor = sqlConnection.cursor()
    query = """INSERT INTO information(name,contact,instagram,confirmation,count,cost) VALUES (?,?,?,?,?,?) """
    cursor.execute(query,(name_db,contact_db,instagram_db,confirmation_db,count_db,cost_db))
    sqlConnection.commit()
    sqlConnection.close()


def deleteDB():
    name = input("Enter a Name to delete that person from Database : ").lower()
    name_lookup = lookupDB(name)
    delete_id = -1
    if (name_lookup != False):
        delete_id = int(name_lookup[0])
        sqlConnection = sqlite3.connect("party.db")
        cursor = sqlConnection.cursor()
        query = f"DELETE FROM information WHERE id = {delete_id}"
        cursor.execute(query)
        sqlConnection.commit()
        sqlConnection.close()


def showDB():
    print("show is working\n")
    action = input("Enter a name or Enter all : ").lower()
    sqlConnection = sqlite3.connect("party.db")
    cursor = sqlConnection.cursor()
    cursor.execute("SELECT COUNT(name) FROM information")
    rows  = tuple([i+1 for i in range(int(cursor.fetchall()[0][0]))])
    cursor.execute(f"SELECT name,contact,confirmation,count,cost,instagram FROM information where id IN {rows} ")
    result = cursor.fetchall()
    
    if (action == "all") :
        print("\n\n")
        print(tabulate(result,headers = ["name","contact","confirmation","count","cost","instagram"]))
    else:
        temp = []
        for row in result:
            if action in row:
                temp.append(row)
                print("\n\n")
                print(tabulate(temp,headers = ["name","contact","confirmation","count","cost","instagram"]))
    sqlConnection.close()


def updateDB():
    print("Build in progress")

def action_to_perform():
    print ("\nChoose one of the following actions to perform")
    print ("\nTo insert a new person into the database : i \nTo update an existing person's information : u\nTo delete an existing person's information : d\nTo show a person's information : s\nTo exit the program : x")
    action = input("\nuser : ").lower()
    if (action == 'i' or action == 'u' or action == 'd' or action == 's' or action == "x"):
        return action
    

def perform_action(action):
    if (action == "i"):
        insertDB()
    if (action == "d"):
        deleteDB()
    if (action == 's'):
        showDB()
    if (action == 'u'):
        updateDB()



def main():
    action = action_to_perform()
    while action != "x":
        perform_action(action)
        action = action_to_perform()
    

if __name__ == "__main__":
    main()
