import sqlite3
from Model.Singletone import  Singleton
from Model.UserModel import UserModel
from DataObjects.User import User

class DBConnection(metaclass=Singleton):
    def __init__(self):
        super(DBConnection, self).__init__()
        self.conn = sqlite3.connect('resources/TenderDB.db')
        self.cur = self.conn.cursor()

    def createUser(self, username, password, firstname, lastname, location):
        try:
            self.cur.execute("INSERT INTO users VALUES (?,?,?,?,?);", (username,
                                                                       password, firstname, lastname, location))
            self.conn.commit()
        except Exception as e:
            return False
        return True

    def loginUser(self, username, password):
        self.cur.execute("SELECT * from users WHERE username=? AND password=?;", (username, password))
        res = self.cur.fetchall()
        if len(res) == 1:
            UserModel().setUser(User(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4]))

        return len(res)>0

    def createPost(self, seller, model, year, color, distance_driven, image, price, description ):
        self.cur.execute("INSERT INTO posts VALUES (?,?,?,?,?,?,?,?);", (seller, model, year, color,
                                                                           distance_driven, image, price, description))
        self.conn.commit()

    def readPost(self, id):
        self.cur.execute("SELECT * From posts WHERE id=?;",(id,))
        return self.cur.fetchall()

    def allPosts(self, username):
        self.cur.execute("SELECT * From Posts;")
        tempResults = self.cur.fetchall()
        self.cur.execute("SELECT POSTID From Preferences WHERE username =?;", (username,))
        toRemove = self.cur.fetchall()
        for entry in toRemove:
            for i in range(len(tempResults)):
                if entry[0] == tempResults[i][0]:
                    tempResults.pop(i)
                    break
        return tempResults

    # 1 for like, 0 for dislike
    def likePost(self,postid):
        self.cur.execute("INSERT into Preferences VALUES (?,?,?);", (postid, UserModel().user.username , 1))
        self.conn.commit()

    def dislikePost(self,postid):
        self.cur.execute("INSERT into Preferences VALUES (?,?,?);", (postid, UserModel().user.username, 0))
        self.conn.commit()

    def viewLiked(self):
        self.cur.execute("SELECT * FROM Posts INNER JOIN Preferences on Posts.POSTID = Preferences.POSTID WHERE Preference = ? AND username = ?;", (1 , UserModel().user.username))
        return self.cur.fetchall()
