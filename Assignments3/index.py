from flask import Flask, jsonify, render_template, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost',
                     user='root',
                     password='12345678',
                     db='laptop',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
    # Lấy danh sách sản phẩm từ database
    # products = db.get_laptops()

    # Render template 'index.html' và truyền danh sách sản phẩm vào biến 'products' trong context
    # return render_template('index.html', products=products)


@app.route('/laptops', methods=['GET'])
def get_laptops():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM laptopbestseller')
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/laptops', methods=['POST'])
def add_laptop():
    data = request.get_json()
    name = data['Name']
    brand = data['Brand']
    old_price = data['OldPrice']
    new_price = data['NewPrice']
    percent_discount = data['PercentDiscount']
    best_seller = data['BestSeller']
    cursor = db.cursor()
    query = 'INSERT INTO laptopbestseller (Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller) VALUES (%s, %s, %s, %s, %s, %s)'
    values = (name, brand, old_price, new_price, percent_discount, best_seller)
    cursor.execute(query, values)
    db.commit()
    return 'Laptop added'


@app.route('/laptops/<int:id>', methods=['PUT'])
def update_laptop(id):
    data = request.get_json()
    name = data['Name']
    brand = data['Brand']
    old_price = data['OldPrice']
    new_price = data['NewPrice']
    percent_discount = data['PercentDiscount']
    best_seller = data['BestSeller']
    cursor = db.cursor()
    query = 'UPDATE laptopbestseller SET Name=%s, Brand=%s, OldPrice=%s, NewPrice=%s, PercentDiscount=%s, BestSeller=%s WHERE id=%s'
    values = (name, brand, old_price, new_price,
              percent_discount, best_seller, id)
    cursor.execute(query, values)
    db.commit()
    return 'Laptop updated'


@app.route('/laptops/<int:id>', methods=['DELETE'])
def delete_laptop(id):
    cursor = db.cursor()
    query = 'DELETE FROM laptopbestseller WHERE id=%s'
    values = (id,)
    cursor.execute(query, values)
    db.commit()
    return 'Laptop deleted'


if __name__ == '__main__':
    app.run()
