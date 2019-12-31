from Model.DBConnection import DBConnection
import kivy
from kivy.properties import ObjectProperty

class Register:
    username= ObjectProperty(None)
    password= ObjectProperty(None)
    firstName= ObjectProperty(None)
    lastName= ObjectProperty(None)
    location= ObjectProperty(None)

    def register(self):
        db = DBConnection()
        db.createUser(self.username.text, self.password.text, self.firstName.text, self.lastName.text, self.location.text)
        return True

