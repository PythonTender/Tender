from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
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

from Controller.Login import Login
from Controller.Register import Register
from Controller.PostView import PostView
from Controller.WishList import WishList


from Model.WishListModel import WishListModel



LabelBase.register(name='Gotham Rounded',fn_regular='resources/fonts/Gotham Rounded Light.otf',fn_bold='resources/fonts/Gotham Rounded Bold.otf')

Builder.load_file('View/screenmanager.kv')

class ScreenLogin(Screen):
    def __init__(self, **kwargs):
        super(ScreenLogin, self).__init__(**kwargs)
        self.add_widget(Login(model=DBModel()))

class ScreenRegister(Screen):
    def __init__(self, **kwargs):
        super(ScreenRegister, self).__init__(**kwargs)
        self.add_widget(Register(model=DBModel()))

class ScreenPostView(Screen):
    postview = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(ScreenPostView,self).__init__(**kwargs)
        self.postview = PostView(model=PostViewModel(DBModel()))
        self.add_widget(self.postview)
    def on_pre_enter(self, *args):
        self.postview._init_post_view()

class ScreenWishList(Screen):
    wishlist = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ScreenWishList, self).__init__(**kwargs)
        self.wishlist = WishList(model=WishListModel(DBModel()))
        self.add_widget(self.wishlist)
    def on_pre_enter(self, *args):
        self.wishlist._init_post_view()

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenLogin(name="login_screen"))
screen_manager.add_widget(ScreenRegister(name="register_screen"))
screen_manager.add_widget(ScreenPostView(name="postview_screen"))
screen_manager.add_widget(ScreenWishList(name="wishlist_screen"))

class TenderApp(App):
    def __init__(self):
        App.__init__(self)


    def build(self):
        return screen_manager



tender = TenderApp()

tender.run()
