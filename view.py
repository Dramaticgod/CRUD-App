#This python script takes all the user input and passes it into the controller which then connects it with the database

import controller
import pprint

def view_user_command_prompt():
    print ("\nChoose one of the following actions to perform")
    print ("\nTo insert a new person into the database : i \nTo update an existing person's information : u\nTo delete an existing person's information : d\nTo show a person's information : s\nTo exit the program : x")
    action = input("\nuser : ").lower()
    if (action == 'i' or action == 'u' or action == 'd' or action == 's'):
        return action
    elif(action == "x"):
        return False
    else:
        return f"wrong command entered, please look at the options again"

def view_insert_command():
        name = input("Name : ").lower()
        contact = input("Phone Number : ")
        instagram = input("Instagram : ")
        confirmation = input("Are they attending yes/no ?  :  ").lower()
        count = int(input("How many people including the person attending: "))       
        print(controller.controller_insert_DB(name,contact,instagram,confirmation,count))

def view_delete_command():
        name = input("Enter a Name to delete from the database : ").lower()
        duplicate = controller.controller_check_duplicates(name)
        if( duplicate[0] == True):
            print(duplicate[1])
            id = int(input("Enter a id from above to delete : "))
            rows = duplicate[2]
            for tupl in rows:
                if tupl[0] == id:
                    print(controller.controller_delete_using_ID_DB(name,id))
        else:
            print(controller.controller_delete_DB(name))

def view_show_command():
        action = input("Enter a name or Enter all : ").lower()
        if (action == "all"):
            print(controller.controller_show_all_DB())
        else:
            print(controller.controller_show_one_DB(action))
        #TODo : show duplicates if exists for this

def view_update_command():
     name = input("Enter a name : ").lower()
     data = controller.controller_dictionary_by_name(name)
     if(data == None):
        print("name not found in database")
     else:
            print("\nEnter what you like to change (name/contact/cost/confirmation/instagram/count) one by one \n Once finished press x to exit")
            while True:
                change = input("\nEnter what you would like to change : ").lower()
                if change in data.keys():
                    new = input(f"\nEnter the new value for {change} : ").lower()
                    data[change] = new
                elif change == "x":
                     break
                else:
                    print("wrong variable entered please type one of the following confirmation,contact,cost,count,instagram,name")
            print(controller.controller_update_DB(data))
     #print(data)
                     

def view_perform_command(action):
    if (action == "i"):
        view_insert_command()
    
    elif (action == "d"):
        view_delete_command()

    elif (action  == "s"):
        view_show_command()
    
    elif (action == "u"):
         view_update_command()
    
def view_user_prompt():
    while True:
        action = view_user_command_prompt()
        if action == False:
            break
        view_perform_command(action)

if __name__ == '__main__':
    view_user_prompt()