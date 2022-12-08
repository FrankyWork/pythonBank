# Money transfer service

import json


def get_date(login_user, password_user):
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        try:
            if login_user == data[login_user]["login"]:
                print("Login ACCESED")
            else:
                print("NOT READY")
            if password_user == data[login_user]["password"]:
                print("Hello", data[login_user]["name"], data[login_user]["lastName"], "!!!" "\nYour login:",
                      data[login_user]["login"], "\nYour balance:", data[login_user]["balance"])
            else:
                print("NOT READY")
        except KeyError:
            print("Bad try!")


class User:
    _name = None
    _lastName = None
    _login = None
    _password = None
    _balance = None

    def __init__(self, _name, _lastName, _login, _password, _balance):
        get_date(_login, _password)
        self.gat_user(_name, _lastName, _login, _password, _balance)

    def gat_user(self, _name=None, _lastName=None, _login=None, _password=None, _balance=None):
        self._name = _name
        self._lastName = _lastName
        self._login = _login
        self._password = _password
        self._balance = _balance


login = input("Login:")
password = input("Password:")

user = User("None", "None", login, password, 0)
