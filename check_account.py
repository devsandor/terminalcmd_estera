import pickle
import os
from mdl.User import *
i = 0
def pickle_save(variable,way,mo):
    str(way)
    if 'r' in mo:
        with open(way, "rb") as file:
            unpickler = pickle.Unpickler(file)
            list_id = unpickler.load()
    elif 'w' in mo:
        with open(way, "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(variable)
    else:
        print("Erreur")
while i == 0:
    user_choice = input("> ")
    user_entry = user_choice.split(" ")
    if user_entry[0] == "login" and  len(user_entry) == 3:
        if user_entry[1] == "admin" and user_entry[2] == "81":
            i = 1
        else:
            print(">Wrong password\n")
    elif user_entry[0] == "cls":
        os.system('cls')
    else:
        pass
i = 0
while i == 0:
    with open("data/account", "rb") as file:
        unpickler = pickle.Unpickler(file)
        list_id = unpickler.load()
    user_choice = str(input("> ")).lower()
    if user_choice == "create":
        try:
            user_choice = str(input("New name> "))
            user_choice1 = str(input("New password> "))
            user_choice2 = str(input("New status> "))
        except:
            print("Error , would you enter a string")
        else:
            user = User(user_choice, user_choice1)
            user.status = user_choice2
            print(f"{user.name} is created")
            print(f"Password:{user.password}\nConnection number:{user.connection_number}\nStatus:{user.status}")
    elif user_choice == "edit":
        user_choice = input("name or password ?> ")
        if user_choice == "name":
            user_choice = str(input("account name> "))
            user_choice1 = str(input("new name> "))
            for a, user in enumerate(list_id):
                if user.name == user_choice:
                    user.name = user_choice1
                    print(f"{user.name} a été modifié")
                    list_id[a] = user
                    pickle_save(list_id, "data/account", "wb")
        elif user_choice == "password":
            user_choice = str(input("account name> "))
            user_choice1 = str(input("new password>"))
            for a, user in enumerate(list_id):
                if user.password == user_choice:
                    user.password = user_choice1
                    print(f"{user.name} a été modifié")
                    list_id[a] = user
                    pickle_save(list_id, "data/account", "wb")
        else:
            print("e")
    elif user_choice == "delete":
        user_choice = str(input("account name> "))
        user_choice1 = str(input(f"Are you sure removed {user_choice}"))
        if user_choice1 == "yes" or user_choice1 == "y" or user_choice1 == "oui":
            print("e")
            for a, user in enumerate(list_id):
                if user.name == user_choice:
                    print(f"{user_choice} removed")
                    del list_id[a]
                    del user
                    pickle_save(list_id, "data/account", "wb")
        else:
            pass
    elif user_choice == "list_account":
        for a, user in enumerate(list_id):
            print(f"Name:{user.name}\nPassword:{user.password}\nConnection number{user.connection_number}\nStatus:{user.status}")
    elif user_choice == "cls":
        os.system('cls')
    elif user_choice == "help":
        print("print - print the ids\ncls - Clear\nlist_account - print the list of users\ndelete - delete account\nedit - edit a account\ncreate - create a new account")
    elif user_choice == "print":
        user_choice == str(input("all/name/nb_connection/status/password> "))
        if user_choice == "all":
            print(f"Name:{user.name}")
            print(f"Password:{user.password}\nConnection number:{user.connection_number}\nStatus:{user.status}")
        elif user_choice == "name":
            for user in list_id:
                print(f"Name:{user.name}")
        elif user_choice == "password":
            for user in list_id:
                print(f"password:{user.password}")
                print(f"id:{user.ids}")
        elif user_choice == "nb_connection":
            for user in list_id:
                print(f"Connection number:{user.connection_number}")
        elif user_choice == "status":
            for user in list_id:
                print(f"Status:{user.status}")
        else:
            pass
    else:
        pass
