import sqlite3

class db :

    def __init__(self):
        self.conn = sqlite3.connect('lite.db')
        self.cur = self.conn.cursor()
        self.id = 1

    def createUser(self, username, firstname, lastname, password, location):
        self.cur.execute("INSERT INTO users VALUES (?,?,?,?,?);",username,firstname,lastname,password,location)
        self.conn.commit()

    def loginUser(self, username, password):
        self.cur.execute("SELECT * from users WHERE username=? AND password=?;",username, password)
        res = cur.fetchall()
        return res is not none

    def createPost(self, seller, model, year, color, distance_driven, image, price, description ):
        self.cur.execute("INSERT INTO posts VALUES (?,?,?,?,?,?,?,?,?);", self.id, seller, model, year, color, distance_driven, image, price, description)
        self.conn.commit()
        self.user += 1

    def readPost(self, id):
        self.cur.execute("SELECT * From posts WHERE id=?;",id)
        return cur.fetchall()

    def allPosts(self):
        self.cur.execute("SELECT * From posts;")
        return cur.fetchall()

    # 0 for like, 1 for dislike
    def likePost(self,postid):
        self.cur.execute("INSERT into wishlist VALUES (?,?,?);", postid, self.username, 0)
        self.conn.commit()

    def dislikePost(self,postid):
        self.cur.execute("INSERT into wishlist VALUES (?,?);", postid, self.username, 1)
        self.conn.commit()

    def viewLiked(self):
        self.cur.execute("SELECT * FROM wishlist WHERE liked = ? AND username = ?;", 0 , self.username)
        return curr.fetchall()