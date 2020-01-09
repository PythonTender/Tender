from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from Controller.WishListItem import WishListItem
from Controller.WishListView import RecycleWishlist
from kivy.clock import Clock
# from kivy.uix.screenmanager import Screen
from DataObjects.Post import Post



class WishList(BoxLayout):

    lv = ObjectProperty(None)
    Posts = ListProperty([])

    def __init__(self, **kwargs):
        super(WishList, self).__init__()
        self.model = kwargs.get('model',None)
        self.model.set_view(self)
        self.bind(Posts=self.refresh)

    def btnPressed(self, numPressed):
        print ("Pressed " + str(numPressed))


        # for post in postsLiked:
        #     label = Label(text = post.model + " ," + post.color + " - " + post.price +"$")
        #     label.id = post.id
        #     self.add_widget(label)

    def refresh(self,instance, value):
        self.lv.data.clear()
        self.lv.data = [{'Post': x} for x in self.Posts]

    def set_posts(self, posts):
        self.Posts = posts

    def _init_post_view(self,dt=0):
        self.model.refresh_post_view()

class MyApp(App):
    def build(self):
        return WishList()

if __name__ == "__main__":
    MyApp().run()