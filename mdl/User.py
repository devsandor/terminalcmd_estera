import pickle 
import random
class User():
    nb_created_account = int(0)
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._connection_number = int(0)
        self._status = "default"
    def get_name(self):
        return self._name
    def get_password(self):
        return self._password
    def get_status(self):
        return self._status
    def get_connection_number(self):
        return self._connection_number
    def get_nb_created_account(cls):
        return User.nb_created_account
    def set_name(self, name):
        self._name = name
    def set_password(self, password):
        self._password = password
    def set_status(self, status):
        self._status = status
    def set_connection_number(self, connection_number):
        self._connection_number = connection_number
    def set_nb_created_account(cls, nb_created_account):
        User.nb_created_account = nb_created_account
    name = property(get_name, set_name, None, "User name")
    password = property(get_password, set_password, None, "User password")
    connection_number = property(get_connection_number, set_connection_number)
    status = property(get_status, set_status)
    get_nb_created_account = classmethod(get_nb_created_account)
    set_nb_created_account = classmethod(set_nb_created_account)

def User_class_check():
    with open('data.account', 'rb') as file:
        unpickler = pickle.Unpickler(file)
        list_id = unpickler.load()
    User.i = list_id[0]
