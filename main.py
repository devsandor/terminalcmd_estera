import time
import os
from mdl.func import  *
from mdl.User import *

i = int(0)
user_now = None
while i == 0:
    tline1 = time.strftime("%d:%m:%Y-%H:%M:%S")
    tline = "{} default> ".format(tline1)
    user_choice = str(input("{0}".format(tline)))
    if len(user_choice) <= 0:
        input(f'{tline}Please reenter"{user_choice}" is not correct')
    elif user_choice == "help":
        help_cmd()
    else:
        list_entry = user_choice.split(" ") 
        if len(list_entry) < 3:
            print(f"{tline}Please enter a correcte command")
            continue
        else:
            tpl = sort_lr(list_entry)
            #recupere un tuple contenant i = 1 et user_now ou juste i = 0
            if type(tpl) == tuple:
                i = tpl[0]
                user_now = tpl[1]
i = 0
while i == 0:
    tline = f"{tline1} {user_now.name}> "
    user_choice = str(input(f"{tline}"))
    if not len(user_choice) < 3:
        a = 0
        list_entry = user_choice.split(" ")
        for cmd in list_cmd:
            if cmd == list_entry[0]:
                (i, user_ret) = sort_commands(list_entry, user_now)
                if user_ret != 81:
                    user_now = user_ret
                else:
                    break
            elif a >= len(list_cmd):
                print(f"{tline}Please enter a correct command")
            a += 1
if i == 2:
    print(f"{tline}You're log out because you deleted your account")
