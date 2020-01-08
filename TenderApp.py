from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from Controller.PostView import PostView
from Controller.WishListView import RecycleWishlist
from Controller.WishList import WishList
from Model.PostViewModel import PostViewModel
from Model.DBModel import DBModel
from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase

from Controller import Login, Register, PostView, WishList

from Model.WishListModel import WishListModel

LabelBase.register(name='Gotham Rounded',fn_regular='resources/fonts/Gotham Rounded Light.otf',fn_bold='resources/fonts/Gotham Rounded Bold.otf')

Builder.load_file('View/screenmanager.kv')


class ScreenLogin(Screen):
    pass

class ScreenRegister(Screen):
    pass

class ScreenPostView(Screen):
    pass

class ScreenWishList(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenLogin(name="login_screen"))
screen_manager.add_widget(ScreenRegister(name="register_screen"))
screen_manager.add_widget(ScreenPostView(name="postview_screen"))
screen_manager.add_widget(ScreenWishList(name="wishlist_screen"))

class TenderApp(App):
    def __init__(self):
        App.__init__(self)


    def build(self):
        # return PostView(model=PostViewModel(DBModel()))
        # return WishList(model=WishListModel(DBModel()))
        # return WishList(model=WishListModel(DBModel()))
        # return MenuBar()
        return screen_manager

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

tender = TenderApp()

tender.run()
