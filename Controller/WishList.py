from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget

from DataObjects.Post import Post


posts = []
posts.append(Post("1", "admin", "BMW", "2010", "Blue", "110,000", "BLOB", "550", "New car available!"))

class RecycleWishlist(RecycleView):

    def __init__(self, **kwargs):
        super(RecycleWishlist, self).__init__(**kwargs)
        self.data = [{'text': str(x), 'on_press': self.btnPressed(x)} for x in range (20)]

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