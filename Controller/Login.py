from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from Model import DBModel
from Model.DBConnection import DBConnection


class Login(GridLayout):

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Login, self).__init__()
        self.model = kwargs.get('model',None)

    def validateUser(self):
        if self.model.loginUser(self.username.text, self.password) is not None:
            return True
        return False