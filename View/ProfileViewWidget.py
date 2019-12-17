from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label



class ProfileViewWidget(BoxLayout):
    def __init__(self,post,**kwargs):
        BoxLayout.__init__(self,**kwargs)
        self._post = post
        self._init_widget()


    @property
    def post(self):
        return self._post

    def _init_widget(self):

        im_image = Image(source = self.post.image,size_hint = (1,0.9))
        l_model_year = Label(text="%s,%d" %(self.post.model,self.post.year),halign= 'left',size_hint= (None, None))

        self.add_widget(im_image)
        self.add_widget(l_model_year)

