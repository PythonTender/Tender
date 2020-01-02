from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from Controller.WishListItem import WishListItem
from kivy.clock import Clock
# from kivy.uix.screenmanager import Screen
from DataObjects.Post import Post

#Builder.load_file('View/wishlist_view.kv')

class RecycleWishlist(RecycleView):

    def __init__(self, **kwargs):
        super(RecycleWishlist, self).__init__(**kwargs)

    def btnPressed(self, numPressed):
        print ("Pressed " + str(numPressed))


        # for post in postsLiked:
        #     label = Label(text = post.model + " ," + post.color + " - " + post.price +"$")
        #     label.id = post.id
        #     self.add_widget(label)


class MyApp(App):
    def build(self):
        return RecycleWishlist()

if __name__ == "__main__":
    MyApp().run()