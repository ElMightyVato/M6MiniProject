from flask import Blueprint, request, jsonify
from data_model import database, Product

ProductAPI = Blueprint('ProductAPI', __name__)

@ProductAPI.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock_level=data.get('stock_level', 0))
    database.session.add(new_product)
    database.session.commit()
    return jsonify({'message': 'Product added'}), 201

@ProductAPI.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'name': product.name, 'price': product.price, 'stock_level': product.stock_level})

@ProductAPI.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    product.name = data['name']
    product.price = data['price']
    product.stock_level = data.get('stock_level', product.stock_level)
    database.session.commit()
    return jsonify({'message': 'Product updated'})

@ProductAPI.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    database.session.delete(product)
    database.session.commit()
    return jsonify({'message': 'Product deleted'})