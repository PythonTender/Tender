from Controller.Login import Login
from Controller.PostView import PostView
from Controller.ProfileViewWidget import ProfileViewWidget
from kivy.app import App

class TenderApp(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        return PostView()

tender = TenderApp()

tender.run()