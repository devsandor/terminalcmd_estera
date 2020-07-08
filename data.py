import pickle
import os
import time
from mdl.func import *
s_date = time.ctime()
with open("data/account", "rb") as file:
    unpickler = pickle.Unpickler(file)
    list_id = unpickler.load()
with open("data/accounts.txt", "w") as file:
    file.write(f"{version} - {s_date}\n")
    for user in list_id:
        file.write(f"Name: {user.name}\n")
        file.write(f"Password: {user.password}\n")
        file.write(f"Connection number: {user.connection_number}\n")
        file.write(f"Status: {user.status}\n")
