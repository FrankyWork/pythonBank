# Money transfer service

import Authentication.authentication as auth


class User:
    _name = None
    _lastName = None
    _login = None
    _password = None
    _balance = None

    def __init__(self, _name, _lastName, _login, _password, _balance):
        self.gat_user(_name, _lastName, _login, _password, _balance)

    def gat_user(self, _name=None, _lastName=None, _login=None, _password=None, _balance=None):
        self._name = _name
        self._lastName = _lastName
        self._login = _login
        self._password = _password
        self._balance = _balance


login = input("Login:")
password = input("Password:")

auth.get_date(login, password)

authorization = User("None", "None", login, password, 0)
