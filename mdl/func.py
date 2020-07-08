import os
import pickle
import time
import datetime
from mdl.User import *
dict_color = {"kaki":"6","light_blue":"9", "dark_blue":"1", "grey_blue":"3","light_green":"A", "green":"2", "cyan":"B","red":"C", "pink":"D", "grey":"8", "light_grey":"7", "black":"0", "purple":"5", "yellow":"E", "white":"F"}
user_now = User("default", "81")
tline1 = time.strftime("%d:%m:%Y-%H:%M:%S")
tline = "{} {}> ".format(tline1, user_now.name)
list_cmd = ["list_account","cls", "pause", "help", "color", "exit", "user_account", "version", "date", "time", "credit"]
list_color = ["A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"]
#dict_color = ["blue":blue_c(1),"dark_blue":blue_d(1),"green":green_c(1),"dark_green":green_d,"grey":grey,"light_grey":grey_c,"red":red,"pink":pink,"black":black,"white":white,"yellow":yellow,"brown":brown,"kaki":kaki,"cyan":cyan]
#Sort the commands next the login/register part
def sort_commands(user_entry, user_now):
    if user_entry[0] == "list_account":
        user_entry.append(4)
        if user_entry[1] == "814507hE" or user_now.status == "admin":
            with open("data/account", "rb") as file:
                unpickler = pickle.Unpickler(file)
                list_account = unpickler.load()
            for user in list_account:
                print(f"Name : {user.name} Password : {user.password}")
            return 0, 81
        else:
            print(f"{tline}Wrong Password")
            return 0, 81
    elif user_entry[0] == "cls":
        os.system("cls")
        return 0, 81
    elif user_entry[0] == "pause":
        if type(user_entry[1]) != int():
            try:
                user_entry[1] = int(user_entry[1])
            except:
                print(f"{tline}Please enter a correct parameter 'pause number_seconds'")
                return 0, 81
        seconds = user_entry[1]
        time.sleep(seconds)
    elif user_entry[0] == "help":
        help_cmd()
        return 0, 81
    elif user_entry[0] == "exit":
        return 1, 81
    elif user_entry[0] == "color":
        if len(user_entry) == 0:
            print(f"{tline}Please enter a correct parameter 'color write_color background_color'")
            return 0, 81
        elif len(user_entry[1]) == 1 or len(user_entry[1]) == 2:
            for elt in list_color:
                try:
                    os.system(f"color {elt}")
                except:
                    print(f"{tline}Please enter a correct parameter color write_color+background_color")
                else:    
                    return 0, 81
        print(f"{tline}Please enter a correct parameter 'color write_color background_color'")
        return 0, 81
    elif user_entry[0] == "user_account":
        try:
            with open("data/account", "rb") as file:
                unpickler = pickle.Unpickler(file)
                list_id = unpickler.load()
        except:
            return 0, 81
        if len(user_entry) != 3:
            print(f"{tline}Please enter corrects parameters 'user_account edit/delete name/password")
            return 0, 81
        if user_entry[1] == "edit":
            if user_entry[2] == "name":
                user_choice = str(input(f"{tline}Do you want change the name> "))
                if user_choice == "yes" or user_choice == "y" or user_choice == "oui":
                    user_choice = str(input(f"{tline}New name> "))
                    for i, user in enumerate(list_id):
                        if user.name == user_now.name:
                            user_now.name = user_choice
                            user.name = user_now.name
                            list_id[i] = user
                            with open('data/account', 'wb') as file:
                                pickler = pickle.Pickler(file)
                                pickler.dump(list_id)
                            return 0, user_now
                else:
                    print(f"{tline}Please enter a correct answer")
                    return 0, 81
            elif user_entry[2] == "password":
                user_choice = str(input(f"{tline}Do you want change the password> "))
                if user_choice == "yes" or user_choice == "y" or user_choice == "oui":
                    user_choice = str(input(f"{tline}New password> "))
                    for i, user in enumerate(list_id):
                        if user.password == user_now.password:
                            user_now.password = user_choice
                            user.password = user_now.password
                            list_id[i] = user
                            with open('data/account', 'wb') as file:
                                pickler = pickle.Pickler(file)
                                pickler.dump(list_id)
                            return (0, user_now)
                else:
                    print(f"{tline}Please enter a correct answer")
                    return 0, 81
            else:
                print(f"{tline}Please enter correct parameters")
                return 0, 81
        elif user_entry[1] == "delete":
            user_choice = input(f"{tline}Are you sure remove the {user_now.name}> ")
            if user_choice == "yes" or user_choice == "oui" or user_choice == "o" or user_choice == "y":
                for i, user in enumerate(list_id):
                    if user_now.name == user.name:
                        print(f"{tline}{user_now.name} is deleted")
                        del list_id[i]
                        with open("data/account", "wb") as file:
                            pickler = pickle.Pickler(file)
                            pickler.dump(list_id)
                        return (2, 81)
            else:
                return (0, 81)
    elif user_entry[0] == "version":
        print(f"Estera v3.1")
    elif user_entry[0] == "date":
        now_time = time.strftime("%H:%M:%S")
        print(now_time)
    elif user_entry[0] == "time":
        now_date = time.strftime("%d:%m:%Y")
        print(now_date)
    elif user_entry[0] == "credit":
        print("Estera v3.1 - 08:07:2020\nDeveloped by Sandor/Progresys\nDistributed by Goldnight Studio")
    else:
        print(f"{tline}Please enter a correct command")
#Sort the login and register
def sort_lr(user_entry):
    admin = User("admin", "81")
    admin1 = User("admin1", "81")
    list_id = [admin, admin1]
    try:
        with open("data/account", "rb") as file:
            munpickler = pickle.Unpickler(file)
            list_id = munpickler.load()
    except:
        with open("data/account", "wb") as file:
            mpickler = pickle.Pickler(file)
            mpickler.dump(list_id)

    if "login" in user_entry:
        for i, user in enumerate(list_id):
            if user_entry[1] == user.name:
                if user_entry[2] == user.password:
                    print(f"{tline}Welcome , you're logged in")
                    user.connection_number += 1
                    user_now = user
                    list_id[i] = user
                    with open("data/account", "wb") as file:
                        pickler = pickle.Pickler(file)
                        pickler.dump(list_id)
                    return 1, user_now
                else:
                    print(f"{tline}Please enter the correct password ")
                    return 0, 81
        f"{tline}Please enter the correct name"
    elif "register" in user_entry:
        for i, user in enumerate(list_id):
            if user_entry[1] == user.name:
                user_choice = input(f"{tline}Do you want to recreate {user.name} ")
                if user_choice.lower() == "oui" or user_choice.lower() == "yes" or user_choice.lower() == "y":
                    user = User(user_entry[1],user_entry[2])
                    user.connection_number += 1
                    user_now = user
                    list_id[i] = user
                    with open("data/account", "wb") as file:
                        pickler = pickle.Pickler(file)
                        pickler.dump(list_id)
                    print(f"{tline}Welcome , you're logged in")
                    return 1, user_now
                elif user_choice.lower() == "non" or user_choice.lower() == "no" or user_choice.lower() == "n":
                    print(f"{tline}Please enter a correct identifiant ")
                    return 0, 81
        with open("data/account", "wb") as file:
            user = User(user_entry[1],user_entry[2])
            list_id.append(user)
            user_now = user
            pickler = pickle.Pickler(file)
            pickler.dump(list_id)
        print(f"{tline}Welcome , you're logged in")
        return 1, user_now
    else:
        print(f"{tline}Please login with login name password or register with register name password ")
def help_cmd():
    print("list_account password - List of the accounts\ncls - clear cmd\npause seconds -  pause\nhelp - help\ncolor write_color+background_color\nexit exit the cmd\nuser_account edit/delete/create name/password\ncredit - informations of the developper")
