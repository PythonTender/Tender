from View.ProfileViewWidget import ProfileViewWidget
from DataObjects.Post import Post
from DataObjects.User import User
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class TenderSwipeWindow(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self,orientation='vertical')
        self.posts = []
        self._init_widget()

    def _init_widget(self):

        user = User('talm', '123', 'Tal', 'Malul', 'beer-sheva')
        post = Post(1, user, 'Mazda3', 2006, 'black', 100, 'resources/images.jpeg',
                    40000, 'good')


        pv = ProfileViewWidget(post, orientation='vertical', size_hint=(0.6, 0.7),pos_hint = {'center_x': 0.5})
        box_layout = BoxLayout(orientation='horizontal',size_hint=(1,0.3))

        btn_ok = Button(text='Yes', size_hint=(0.4, 1))
        btn_details = Button(text='Details', size_hint=(0.3, 1))
        btn_no = Button(text='No', size_hint=(0.4,1))

        box_layout.add_widget(btn_ok)
        box_layout.add_widget(btn_details)
        box_layout.add_widget(btn_no)

        self.add_widget(pv)
        self.add_widget(box_layout)