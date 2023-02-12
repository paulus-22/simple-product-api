from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# ENV Variable for SQLAlchemy for postgres db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# defining data model
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

db.create_all()

# add product
@app.route('/products', methods=['POST'])
def create_product():
    body = request.get_json()
    db.session.add(Product(
        body['name'],
        body['price'],
        body['description']
        body['quantity']
    ))
    db.session.commit()
    return "success adding product"

# get single product by id
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    del product.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)

# get list of products with sorting 
# (using url-parameters "sort" : either "newest", "highest", "lowest", "az", "za")
@app.route('/products', methods=['GET'])
def get_products():
    sort_query = request.args.get('sort')
    products = []
    for product in db.session.query(Product).all():
        del product.__dict__['_sa_instance_state']
        products.append(product.__dict__)
    
    if sort_query == "newest":
        products = sorted(products, key=products.product.created_at)
    elif sort_query == "highest":
        products = sorted(products, key=products.product.price, reverse=True)
    elif sort_query == "lowest":
        products = sorted(products, key=products.product.price)
    elif sort_query == "az":
        products = sorted(products, key=products.product.name)
    elif sort_query == "za":
        products = sorted(products, key=products.product.name, reverse=True)

    return jsonify(products)

