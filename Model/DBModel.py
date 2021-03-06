from Model.DBConnection import DBConnection
from DataObjects.Post import Post
from kivy.core.image import Image as CoreImage
from Model.UserModel import UserModel
from kivy.uix.image import Image
from DataObjects.User import User
import io

class DBModel:
    def __init__(self):
        self.tender_db = DBConnection()
        self.userConnected = None

    def get_user_relevant_post(self):
        rs = self.tender_db.allPosts(UserModel().user.username)
        posts = []

        for record in rs:
            p_id = record[0]
            p_seller = record[1]
            p_model = record[2]
            p_year = record[3]
            p_color = record[4]
            p_distance_driven = record[5]
            p_image = record[6]
            p_price = record[7]
            p_description = record[8]

            im = CoreImage(io.BytesIO(p_image), ext="jpg")

            p = Post(p_id, p_seller, p_model, p_year, p_color, p_distance_driven, im, p_price, p_description)
            posts.append(p)

        return posts

    def get_user_relevant_wl_post(self):
        rs = self.tender_db.viewLiked()
        posts = []

        for record in rs:
            p_id = record[0]
            p_seller = record[1]
            p_model = record[2]
            p_year = record[3]
            p_color = record[4]
            p_distance_driven = record[5]
            p_image = record[6]
            p_price = record[7]
            p_description = record[8]

            im = CoreImage(io.BytesIO(p_image), ext="jpg")

            p = Post(p_id, p_seller, p_model, p_year, p_color, p_distance_driven, im, p_price, p_description)
            posts.append(p)

        return posts

    def update_wish_list(self, post, is_wished):
        pass
        if (is_wished):
           self.tender_db.likePost(postid=post.id)
        else:
            self.tender_db.dislikePost(postid=post.id)

    def loginUser(self, username, password):
        if self.tender_db.loginUser(username, password):
            self.userConnected = username
            return True
        return False

    def createUser(self, username, password, firstname, lastname, location):
        return self.tender_db.createUser(username, password, firstname, lastname, location)