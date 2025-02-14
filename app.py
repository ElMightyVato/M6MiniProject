from flask import Flask
from routes.customers import CustomerAPI
from routes.customer_accounts import CustomerAccountAPI
from routes.orders import OrderView
from routes.products import ProductAPI
from data_model import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:NeroZero1377#@localhost/ecommerce_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Start the database
database.init_app(app)

# Register Blueprints
app.register_blueprint(CustomerAPI)
app.register_blueprint(CustomerAccountAPI)
app.register_blueprint(OrderView)
app.register_blueprint(ProductAPI)

# Home screen route
@app.route('/')
def home():
    return "Welcome to my e-commerce application!"

if __name__ == '__main__':
    app.run(debug=True)
