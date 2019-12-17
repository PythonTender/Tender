
class User:
    def __init__(self,username,password,firstname,lastname,location):
        self._username = username
        self._password = password
        self._firstname = firstname
        self._lastname = lastname
        self._location = location

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def location(self):
        return self._location