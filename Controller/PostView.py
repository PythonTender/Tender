

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty
import math
from kivy.uix.image import Image
from kivy.uix.label import Label

Builder.load_file('PostView.kv')

class PostView(BoxLayout):
    pass
    rotate = NumericProperty(0.0)
    def __init__(self):
        super(PostView,self).__init__()

    def on_touch_move(self, touch):
        self.rotate += -math.asin(touch.dx/self.height)*(180/math.pi)
        if self.rotate > 25 or self.rotate < -25:
            print("out")

    def on_touch_up(self, touch):
        if self.rotate > 25 or self.rotate < -25:
            print("out")
        self.rotate = 0.0