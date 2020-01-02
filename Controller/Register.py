from Model.DBConnection import DBConnection
import kivy
from kivy.properties import ObjectProperty

class Register:
    username= ObjectProperty(None)
    password= ObjectProperty(None)
    firstName= ObjectProperty(None)
    lastName= ObjectProperty(None)
    location= ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Register, self).__init__()
        self.model = kwargs.get('model', None)
        self.model.set_view(self)

    def register(self):
        return self.model.createUser(self.username.text, self.password.text, self.firstName.text, self.lastName.text, self.location.text)

