from model import DataModel
from tabulate import tabulate
# connections between model and view, it takes input from view then proceeds to validate the input and then pass it to the database


#takes the user input (parameters) from view and calls model_insert_DB function. Returns an output message given by model_insert function
def controller_insert_DB(name,contact,instagram,confirmation,count):
    cost = count*18
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_insert_DB(name,contact,instagram,confirmation,count,cost) 
    return u


#takes the user input (name) from view and calls check_duplicate. Returns True if duplicate exists else returns False
def controller_check_duplicates(name):
    if (name == ""):
        return f"invalid name"
    u = DataModel.check_duplicate(name)
    return u


#takes the user input (name) from view and calls model_delete_DB. Returns an output message give by model_delete_DB
def controller_delete_DB(name):
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_delete_DB(name)
    return u   


#takes the user input (name,ID) from view and calls model_delete_by_ID_DB. Returns an output message give by model_delete_DB.
#Called when duplicates exist
def controller_delete_using_ID_DB(name,id):
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_delete_using_ID_DB(name,id)
    return u 


#Calls model_show_all_DB and tabulates the list of tuples to print them out in a pretty way. Returns a table of list of tuples
def controller_show_all_DB():
    rows = DataModel.model_show_all_DB()
    return (tabulate(rows,headers = ["name","contact","confirmation","count","cost","instagram"]))


#take the user input (name) from view and calls model_show_one_DB and then performs the same functioning as controller_show_all_DB
def controller_show_one_DB(name):
    row = DataModel.model_show_one_DB(name)
    temp = []
    if name in row:
        temp.append(row)
    return (tabulate(temp,headers = ["name","contact","confirmation","count","cost","instagram"]))


#takes the user input (name) and makes an isntance of DataModel object. 
#Grabs the information about (name) if it exist and returns a dictionary containing that information
def controller_dictionary_by_name(name):
    person = DataModel(name)
    if person.name_exist == False:
        return None
    else:
        data = person.information
        return data


#takes the user input (changed dictionary to be used for SQL query) and makes an instance of DataModel class using that dictionary.
#Performs model_update_DB on the instance of DataModel Class. Returns an output message from model_update_DB
def controller_update_DB(dictionary):
    person = DataModel(dictionary['name'])
    person.information = dictionary
    return person.model_update_DB()


def controller_show_cost():
    results = DataModel.model_show_total_cost()
    return results