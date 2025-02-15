from flask import Blueprint, request, jsonify
from data_model import database, Order

# Create the blueprint for orders
OrderView = Blueprint('OrderView', __name__)

@OrderView.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    total_price = sum(item['price'] for item in data['products'])
    new_order = Order(customer_id=data['customer_id'], total_price=total_price)
    database.session.add(new_order)
    database.session.commit()
    return jsonify({'message': 'Order placed', 'order_id': new_order.id}), 201

@OrderView.route('/orders/<int:id>', methods = ['GET'])
def get_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify({'order_id': order.id, 'customer_id': order.customer_id, 'total_price': order.total_price, 'date_placed': order.date_placed})

@OrderView.route('/orders/customer', methods=['GET'])
def get_orders_by_customer():
    customer_id = request.args.get('customer_id')
    if customer_id:
        orders = Order.query.filter_by(customer_id=customer_id).all()
        if not orders:
            return jsonify({'message': 'No orders found for this customer'}), 404
        return jsonify([{'order_id': order.id, 'total_price': order.total_price, 'date_placed': order.date_placed} for order in orders])
    return jsonify({'message': 'Customer ID is required'}), 400