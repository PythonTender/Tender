from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from DataObjects.Post import Post

posts = []
posts.append(Post("1", "admin", "BMW", "2010", "Blue", "110,000", "BLOB", "550", "New car available!"))

class WishList(Widget):

    def __init__(self, postsLiked):
        super(WishList, self).__init__()
        self.add_widget(Label(text= "Yoink", pos_hint={"y": 0.5, "x" : 0.5}, size= (500, 500)))

        # for post in postsLiked:
        #     label = Label(text = post.model + " ," + post.color + " - " + post.price +"$")
        #     label.id = post.id
        #     self.add_widget(label)


class MyApp(App):
    def build(self):
        return WishList(posts)

if __name__ == "__main__":
    MyApp().run()