from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Initialize the SQLAlchemy object
database = SQLAlchemy()

# Model for the Customer
class Customer(database.Model):
    __tablename__ = 'customers'  # This matches the table name in MySQL

    id = database.Column(database.Integer, primary_key=True)  # Primary key for unique identification
    name = database.Column(database.String(25), nullable=False)
    email = database.Column(database.String(60), unique=True, nullable=False)
    phone_number = database.Column(database.String(10))

    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone_number = phone

    def __repr__(self):
        return f'<Customer {self.name}>' # Remember youre better safe than sorry using
    # table name since MySQL tends to be case sensitive when it comes to referencing them


# Model for the CustomerAccount
class CustomerAccount(database.Model):
    __tablename__ = 'customer_accounts'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(25), unique=True, nullable=False)
    password = database.Column(database.String(150), nullable=False)  

    customer_id = database.Column(database.Integer, database.ForeignKey('customers.id'), nullable=False)
    customer = database.relationship('Customer', backref=database.backref('account', uselist=False))

    def __init__(self, username, password, customer_id):
        self.username = username
        self.password = password
        self.customer_id = customer_id

    def __repr__(self):
        return f'<CustomerAccount {self.username}>'

# Model for the Product
class Product(database.Model):
    __tablename__ = 'products'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    price = database.Column(database.Float, nullable=False)
    stock_level = database.Column(database.Integer, default=0)

    def __init__(self, name, price, stock_level=0):
        self.name = name
        self.price = price
        self.stock_level = stock_level

    def __repr__(self):
        return f'<Product {self.name}>'

# Model for the Order
class Order(database.Model):
    __tablename__ = 'orders'

    id = database.Column(database.Integer, primary_key=True)
    customer_id = database.Column(database.Integer, database.ForeignKey('customers.id'), nullable=False)
    date_placed = database.Column(database.DateTime, default=datetime.utcnow)
    total_price = database.Column(database.Float)

    customer = database.relationship('Customer', backref=database.backref('orders', lazy=True))

    def __init__(self, customer_id, total_price):
        self.customer_id = customer_id
        self.total_price = total_price

    def __repr__(self):
        return f'<Order {self.id}>'
