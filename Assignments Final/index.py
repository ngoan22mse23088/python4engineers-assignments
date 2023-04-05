from laptopseller import LaptopSeller
from flask import Flask, flash, render_template, request
from database import Database

app = Flask(__name__)
app.secret_key = "assignment2"
db = Database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')


@app.route('/edit/<int:id>/', methods=['GET'])
def edit(id):
    laptop = db.get_laptopbestseller_by_id(id)
    print(laptop)
    return render_template('edit.html', laptop=laptop)


@app.route('/edit/<int:id>/', methods=['POST'])
def update_edit(id):
    form = request.form
    name = form.get('name')
    brand = form.get('brand')
    old_price = form.get('oldPrice')
    new_price = form.get('newPrice')
    percent_discount = form.get('percentDiscount')
    best_seller = form.get('bestSeller')
    laptop = LaptopSeller(id, name, brand, old_price,
                          new_price, percent_discount, best_seller)
    if db.update(laptop):
        flash("A laptop has been updated")
    else:
        flash("A laptop can not be updated")
    laptop = db.get_laptopbestseller_by_id(id)
    return render_template('edit.html', laptop=laptop)


@app.route('/laptop', methods=['GET'])
def laptops():
    laptops = db.get_laptopbestsellers()
    return render_template('laptop.html', laptops=laptops)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if db.delete(id):
        flash("A laptop has been deleted")
    else:
        flash("A laptop can not be deleted")
    return laptops()


@app.route('/create', methods=['POST'])
def addlaptop():
    form = request.form
    name = form.get('name')
    brand = form.get('brand')
    old_price = form.get('oldPrice')
    new_price = form.get('newPrice')
    percent_discount = form.get('percentDiscount')
    best_seller = form.get('bestSeller')
    laptop = LaptopSeller(None, name, brand, old_price,
                          new_price, percent_discount, best_seller)
    if db.insert(laptop):
        flash("A laptop has been added")
    else:
        flash("A laptop can not be added")
    return laptops()


@app.errorhandler(404)
def page_not_found():
    error_message = "This is an error message."
    return render_template('error.html', error=error_message)


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
