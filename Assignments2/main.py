from post import Post
from flask import Flask, flash, render_template, request
from database import Database

app = Flask(__name__)
app.secret_key = "assignment2"
db = Database()

import mysql.connector

# Kết nối đến database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="12345678",
#   database="mydatabase"
# )

# Tạo database
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE posts (id int NOT NULL AUTO_INCREMENT,title varchar(255),content varchar(255),PRIMARY KEY (id));")
# mycursor.execute("SELECT * FROM posts")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# print("completed")

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/edit/<int:id>/', methods=['GET'])
def edit(id):
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)

@app.route('/edit/<int:id>/', methods=['POST'])
def update_edit(id):
    form = request.form
    title = form.get('title')
    content = form.get('age')
    post = Post(id, title, content)
    if db.update(post):
        flash("A post has been updated")
    else:
        flash("A post can not be updated")
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)

@app.route('/posts', methods=['GET'])
def posts():
    posts = db.get_posts()
    print(posts)
    return render_template('post.html', posts=posts)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if db.delete(id):
        flash("A post has been deleted")
    else:
        flash("A post can not be deleted")
    return posts()


@app.route('/create', methods=['POST'])
def addphone():
    form = request.form
    title = form.get('title')
    content = form.get('age')
    post = Post(None, title, content)
    if db.insert(post):
        flash("A post has been added")
    else:
        flash("A post can not be added")
    return posts()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
