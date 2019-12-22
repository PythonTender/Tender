from kivy.uix.gridlayout import GridLayout

from View.TenderSwipeWindow import TenderSwipeWindow
from kivy.app import App

class Login(GridLayout):
    pass


class TenderApp(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        return Login()

tender = TenderApp()

tender.run()