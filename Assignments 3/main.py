# Thêm các thư viện cơ bản để xử lý
from post import Post
from flask import Flask, flash, render_template, request
from database import Database
import mysql.connector

app = Flask(__name__)
app.secret_key = "assignment3"
db = Database()

# Kết nối tới MySQL (port mặc định 3306)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="mydatabase"
)

# Tạo table nếu chưa có
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS posts (id int NOT NULL AUTO_INCREMENT,title varchar(255),content varchar(255),PRIMARY KEY (id));")
mycursor.execute("SELECT * FROM posts")
myresult = mycursor.fetchall()

# Trang main
@app.route('/')
def index():
    return render_template('index.html')

# Trang create
@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

# Trang create mới
@app.route('/create', methods=['POST'])
def addPost():
    form = request.form
    title = form.get('title')
    content = form.get('content')
    post = Post(None, title, content)
    if db.insert(post):
        flash("Post has been added")
    else:
        flash("Post can not be added")
    return posts()

# Trang lấy 1 post theo id
@app.route('/edit/<int:id>/', methods=['GET'])
def edit(id):
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)

# Trang cập nhât 1 post theo id
@app.route('/edit/<int:id>/', methods=['POST'])
def update_edit(id):
    form = request.form
    title = form.get('title')
    content = form.get('content')
    post = Post(id, title, content)
    if db.update(post):
        flash("A post has been updated")
    else:
        flash("A post can not be updated")
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)

# Trang get ds post theo id
@app.route('/posts', methods=['GET'])
def posts():
    posts = db.get_posts()
    return render_template('posts.html', posts=posts)

# Trang xóa 1 post theo id
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if db.delete(id):
        flash("A post has been deleted")
    else:
        flash("A post can not be deleted")
    return posts()

# Trang xử lý khi not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
