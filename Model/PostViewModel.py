from Model import DBModel

class PostViewModel:

    def __init__(self,data_model):
        self.data_model = data_model

    def refresh_post_view(self,dt=0):
        if not self.post_view:
            raise Exception('post_view is set to None')

        self.post_view.set_posts(self._get_user_relevant_posts())

    def _get_user_relevant_posts(self):
        return self.data_model.get_user_relevant_post()

    def set_view(self,view=None):
        self.post_view = view

