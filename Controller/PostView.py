from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from Controller.ProfileViewWidget import ProfileViewWidget
from kivy.clock import Clock
import math


Builder.load_file('View/PostView.kv')


class PostView(AnchorLayout):
    rotate = NumericProperty(0.)
    pv_front = ObjectProperty()
    pv_back = ObjectProperty()
    y_translate = NumericProperty(0.)
    Posts = ListProperty([])

    def __init__(self, **kwargs):
        super(PostView, self).__init__()
        self.model = kwargs.get('model',None)
        self.model.set_view(self)
        self.bind(Posts=self.refresh)
        Clock.schedule_once(self._init_post_view)

    def on_touch_move(self, touch):
        self.rotate += -math.asin(touch.dx / self.height) * (180 / math.pi)
        self.y_translate += touch.dy
        if len(self.Posts) > 0 and (touch.x >= self.width-5 or touch.x <= 5):
            self.dispatch('on_touch_up', touch)

    def on_touch_up(self, touch):
        if len(self.Posts) > 0 and (self.rotate > 15 or self.rotate < -15):
            p = self.Posts.pop(0)
            self.model.post_preference(p, self.rotate)
        self.y_translate = 0.
        self.rotate = 0.

    def refresh(self,instance, value):
        if len(self.Posts) > 0:
            self.pv_front.Post = self.Posts[0]
            if len(self.Posts) > 1:
                self.pv_back.Post = self.Posts[1]

    def set_posts(self, posts):
        self.Posts = posts

    def _init_post_view(self,dt=0):
        self.model.refresh_post_view()

    def _model_set_view(self):
        self.model.set_view(self)
