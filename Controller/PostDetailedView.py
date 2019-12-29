from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder


Builder.load_file('View/post_detailed_view.kv')


class PostDetailedView(Popup):
    image = ObjectProperty(None)
    lb_model_year = ObjectProperty(None)
    lb_color_distance_price = ObjectProperty(None)
    lb_description = ObjectProperty(None)
    Post = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PostDetailedView, self).__init__()
        self.bind(Post=self.refresh)
        self.Post = kwargs.get('post',None)

    def refresh(self,instance, value):
        self.image.texture = self.Post.image.texture
        self.lb_model_year.text = '[b]' + str(self.Post.model) + '[/b]' + ', [size=22]' + str(self.Post.year) + '[/size]'
        self.lb_color_distance_price.text =  str(self.Post.color) + '|' + str(self.Post.distance_driven) + "|" + str(self.Post.price)
        self.lb_description.text = str(self.Post.description)

