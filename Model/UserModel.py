
from DataObjects.User import User
from Model.Singletone import Singleton

class UserModel(metaclass=Singleton):
    def __init__(self):
        super(UserModel, self).__init__()
        self.user = None

    def setUser(self,user):
        self.user = user

