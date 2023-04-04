import pymysql
from post import Post

class Database:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="12345678", database="mydatabase", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM posts order by id asc")
            else:
                cursor.execute(
                    "SELECT * FROM posts where id = %s order by id asc", (id))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def get_posts(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT id, title, content FROM posts")
            data = cursor.fetchall()
            return [Post(*post) for post in data]
        except:
            return ()
        finally:
            con.close()
        pass

    def get_post_by_id(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT id, title, content FROM posts WHERE id = %s", (id))
            post = cursor.fetchone()
            return Post(post[0], post[1], post[2])
        except:
            return None
        finally:
            con.close()
        pass

    def insert(self, post):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO posts(title, content) VALUES(%s, %s)",
                           (post.title, post.content))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, post):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE posts set title = %s, content = %s where id = %s",
                           (post.title, post.content, post.id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM posts where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
