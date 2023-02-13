from model import DataModel

# connections between model and view, it takes input from view then proceeds to validate the input and then pass it to the database

def controller_insert_DB(name,contact,instagram,confirmation,count):
    cost = count*18
    if (name == ""):
        return False
    u = DataModel.model_insert_DB(name,contact,instagram,confirmation,count,cost)
    print("controller")    
