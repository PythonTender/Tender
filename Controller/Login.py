from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from Model import DBModel
from Model.DBConnection import DBConnection


class Login(GridLayout):

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def validateUser(self):
        if DBModel.tender_db.loginUser(self.username.text, self.password) is not None:
            db = DBConnection()
            db.userConnected = self.username.text
            return True
        return False