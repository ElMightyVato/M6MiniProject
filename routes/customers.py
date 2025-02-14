from flask import Blueprint, request, jsonify
from data_model import database, Customer

CustomerAPI = Blueprint('CustomerAPI', __name__)

@CustomerAPI.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'], phone_number=data.get('phone'))
    database.session.add(new_customer)
    database.session.commit()
    return jsonify({'message': 'Customer added'}), 201

@CustomerAPI.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customer.query.all()  # Get all customers
    return jsonify([{'id': customer.id, 'name': customer.name, 'email': customer.email, 'phone': customer.phone_number} for customer in customers]), 200

@CustomerAPI.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email, 'phone': customer.phone_number})

@CustomerAPI.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    customer.name = data['name']
    customer.email = data['email']
    customer.phone_number = data.get('phone', customer.phone_number)
    database.session.commit()
    return jsonify({'message': 'Customer updated'})

@CustomerAPI.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    database.session.delete(customer)
    database.session.commit()
    return jsonify({'message': 'Customer deleted'})