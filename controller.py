from model import DataModel
from tabulate import tabulate
# connections between model and view, it takes input from view then proceeds to validate the input and then pass it to the database

def controller_insert_DB(name,contact,instagram,confirmation,count):
    cost = count*18
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_insert_DB(name,contact,instagram,confirmation,count,cost) 
    return u

def controller_check_duplicates(name):
    if (name == ""):
        return f"invalid name"
    u = DataModel.check_duplicate(name)
    return u

def controller_delete_DB(name):
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_delete_DB(name)
    return u   

def controller_delete_using_ID_DB(name,id):
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_delete_using_ID_DB(name,id)
    return u 

def controller_show_all_DB():
    rows = DataModel.model_show_all_DB()
    return (tabulate(rows,headers = ["name","contact","confirmation","count","cost","instagram"]))

def controller_show_one_DB(name):
    row = DataModel.model_show_one_DB(name)
    temp = []
    if name in row:
        temp.append(row)
    return (tabulate(temp,headers = ["name","contact","confirmation","count","cost","instagram"]))

def controller_dictionary_by_name(name):
    person = DataModel(name)
    if person.name_exist == False:
        return None
    else:
        data = person.information
        return data

def controller_update_DB(dictionary):
    person = DataModel(dictionary['name'])
    person.information = dictionary
    return person.model_update_DB()