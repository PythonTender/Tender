from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label

Builder.load_file('ProfileViewWidget.kv')

class ProfileViewWidget(BoxLayout):
    pass
    image = ObjectProperty(None)