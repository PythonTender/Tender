from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

from Controller.PostDetailedView import PostDetailedView
from kivy.uix.popup import Popup


class WishListItem(BoxLayout):
    image = ObjectProperty(None)
    lb_model_year = ObjectProperty(None)
    Post = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(WishListItem, self).__init__(**kwargs)
        self.Post = kwargs.get('post',None)
        self.bind(Post=self.refresh)

    def refresh(self,instance, value):

        self.image.texture = self.Post.image.texture
        self.lb_model_year.text = '[b]' + str(self.Post.model) + '[/b]' + ', [size=22]' + str(self.Post.year) + '[/size]'

    def open_popup(self):
        p = PostDetailedView(post=self.Post)
        p.open()
