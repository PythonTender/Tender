from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from Controller.PostView import PostView
from Controller.WishListView import RecycleWishlist
from Controller.WishList import WishList
from Model.PostViewModel import PostViewModel
from Model.DBModel import DBModel
from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase

from Model.WishListModel import WishListModel

LabelBase.register(name='Gotham Rounded',fn_regular='resources/fonts/Gotham Rounded Light.otf',fn_bold='resources/fonts/Gotham Rounded Bold.otf')

#
# class MenuBar(GridLayout):
#     pass

class TenderApp(App):
    def __init__(self):
        App.__init__(self)


    def build(self):
        # return PostView(model=PostViewModel(DBModel()))
        # return WishList(model=WishListModel(DBModel()))
        return RecycleWishlist()
        # return MenuBar()

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
tender = TenderApp()

tender.run()
