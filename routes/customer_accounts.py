from flask import Blueprint, request, jsonify
from data_model import database, CustomerAccount

CustomerAccountAPI = Blueprint('customer_account_api', __name__)

@CustomerAccountAPI.route('/customer_accounts', methods=['POST'])
def add_customer_account():
    data = request.get_json()
    new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
    database.session.add(new_account)
    database.session.commit()
    return jsonify({'message': 'Customer account created'}), 201

CustomerAccountAPI.route('/customer_accounts', methods=['GET'])
def get_all_customer_accounts():
    accounts = CustomerAccount.query.all()  # Get all customer accounts
    return jsonify([{'id': account.id, 'username': account.username, 'customer_id': account.customer_id} for account in accounts]), 200

CustomerAccountAPI.route('/customer_accounts/<int:id>', methods=['GET'])
def get_customer_account(id):
    account = CustomerAccount.query.get(id)
    if not account:
        return jsonify({'message': 'Customer Account not found'}), 404
    return jsonify({'id': account.id, 'username': account.username, 'customer_id': account.customer_id})

@CustomerAccountAPI.route('/customer_accounts/<int:id>', methods=['PUT'])
def update_customer_account(id):
    data = request.get_json()
    account = CustomerAccount.query.get(id)
    if not account:
        return jsonify({'message': 'Customer Account not found'}), 404
    account.username = data['username']
    account.password = data['password']  # Store encrypted passwords in production
    database.session.commit()
    return jsonify({'message': 'Customer account updated'}), 200

@CustomerAccountAPI.route('/customer_accounts/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    account = CustomerAccount.query.get(id)
    if not account:
        return jsonify({'message': 'Customer Account not found'}), 404
    database.session.delete(account)
    database.session.commit()
    return jsonify({'message': 'Customer account deleted'}), 200
