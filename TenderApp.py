from Controller.PostView import PostView
from Controller.WishList import RecycleWishlist
from Model.PostViewModel import PostViewModel
from Model.DBModel import DBModel
from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase

from Model.WishListModel import WishListModel

LabelBase.register(name='Gotham Rounded',fn_regular='resources/fonts/Gotham Rounded Light.otf',fn_bold='resources/fonts/Gotham Rounded Bold.otf')


class TenderApp(App):
    def __init__(self):
        App.__init__(self)

    def build(self):
        #return PostView(model=PostViewModel(DBModel()))
        return RecycleWishlist(model=WishListModel(DBModel()))
        # return RecycleWishlist()

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
tender = TenderApp()

tender.run()
