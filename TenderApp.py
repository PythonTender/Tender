from Controller.Controllers import *

from View.TenderSwipeWindow import TenderSwipeWindow
from kivy.app import App

class TenderApp(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        return Login()

tender = TenderApp()

tender.run()