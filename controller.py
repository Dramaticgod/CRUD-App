from model import DataModel
from tabulate import tabulate
# connections between model and view, it takes input from view then proceeds to validate the input and then pass it to the database

def controller_insert_DB(name,contact,instagram,confirmation,count):
    cost = count*18
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_insert_DB(name,contact,instagram,confirmation,count,cost) 
    return u

def controller_delete_DB(name):
    if (name == ""):
        return f"invalid name"
    u = DataModel.model_delete_DB(name)
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
