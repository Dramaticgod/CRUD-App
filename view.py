#This python script takes all the user input and passes it into the controller which then connects it with the database

import controller



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
    

def view_perform_command(action):
    if (action == "i"):
        name = input("Name : ").lower()
        contact = input("Phone Number : ")
        instagram = input("Instagram : ")
        confirmation = input("Are they attending yes/no ?  :  ").lower()
        count = int(input("How many people including the person attending: "))       
        controller.controller_insert_DB(name,contact,instagram,confirmation,count)

def view_user_prompt():
    while True:
        action = view_user_command_prompt()
        if action == False:
            break
        view_perform_command(action)

if __name__ == '__main__':
    view_user_prompt()