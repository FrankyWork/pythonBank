# Money transfer service

import json


def get_date(identification, authentication):
    with open("data_file.json", "r") as authorization_date:
        data = json.load(authorization_date)
        try:
            if identification == data[identification]["login"]:
                print("Authorization successfully")
            if authentication == data[identification]["password"]:
                print("Hello", data[identification]["name"], data[identification]["lastName"], "!!!" "\nYour login:",
                      data[identification]["login"], "\nYour balance:", data[identification]["balance"])
        except KeyError:
            print("Authorization failed!")


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

authorization = User("None", "None", login, password, 0)
