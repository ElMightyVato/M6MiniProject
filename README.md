E-Commerce Application
This is a simple e-commerce application built with Flask and MySQL. It allows customers to manage their accounts, place orders, and interact with product listings.

Features
Customers: Customers can be added, updated, and deleted.
Customer Accounts: Customers can have accounts for login (using their username and password).
Products: Admins can manage products including adding, updating, deleting, and retrieving product details.
Orders: Customers can place orders and view their order history.
Project Structure
ecommerce_app
├── app.py                # Main Flask application file
├── data_model.py         # SQLAlchemy models for database tables
├── routes/               # I thought how can I make my code and routes more organized then I realized I could do it by utilizing OOP fundamentals
│   ├── __init__.py       # Empty file to mark the directory as a package noticed nothing would work unless I had this inside of my routes folder after asking the stackoverflow community for advise
│   ├── customers.py      # Routes for managing customer data
│   ├── customer_accounts.py  # Routes for managing customer accounts
│   ├── orders.py         # Routes for managing orders
│   └── products.py       # Routes for managing products

Setup
Clone the Repository:
First you will want to clone the repository by typing this into your vs.code
**git clone https://github.com/ElMightyVato/ecommerce-app.git
cd ecommerce-app**

Create and Activate a Virtual Environment (windows):
Now you will want to create a virtual enviroment, venv, so that you can run flask
**python -m venv venv
venv\Scripts\activate**

Install Dependencies:
Make sure you install these packages before attempting to run the program
Flask:
**pip install Flask**
Flash_SQLAlchemy:
**pip install Flask-SQLAlchemy**
MySQL Connector:
**pip install mysql-connector-python**

Setting Up MySQL Database:
Here I will give you the Scripts I utilized to create my database in MySQL:

**CREATE DATABASE ecommerce_db;**

**USE ecommerce_db;**

**CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(60) NOT NULL UNIQUE,
    phone_number VARCHAR(10)
);**

**CREATE TABLE customer_accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(25) NOT NULL UNIQUE,
    password VARCHAR(150) NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);**

**CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    stock_level INT DEFAULT 0
);**

**CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    date_placed DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_price FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);**

Here is my sample data I created so we could test and verify our gets.
**INSERT INTO customers (name, email, phone_number) VALUES
('John Doe', 'john.doe@example.com', '1234567890'),
('Jane Smith', 'jane.smith@example.com', '0987654321');**

**INSERT INTO customer_accounts (username, password, customer_id) VALUES
('j_dog', 'hashedpassword123', 1),  -- Passwords should be hashed in a real application
('tame_smith', 'hashedpassword456', 2);**

**INSERT INTO products (name, price, stock_level) VALUES
('Product A', 100.0, 50),
('Product B', 200.0, 30),
('Product C', 150.0, 20);**

**INSERT INTO orders (customer_id, total_price) VALUES
(1, 300.0),
(2, 450.0);**

Also, make sure your MySQL credentials in app.py are correct otherwise the program will shoot you an 404 error once you click on the link.

Run the Application:

To run the application:
python app.py
The application will be accessible at http://127.0.0.1:5000/. Once directed there you should be met with a prompt stating:
Welcome to my e-commerce application!

Product API Endpoints
These are the available endpoints for managing products in the e-commerce application.

1. Create a New Product
Endpoint: /products/create
Method: POST
Description: Allows you to add a new product to the database.
Request Body:
**{
    "name": "Product Name",
    "price": 99.99,
    "stock_level": 50
}**
Response:
Status: 201 Created
Body:
**{
    "message": "Product added"

1. Get Product Details
Endpoint: /products/<id>/details
Method: GET
Description: Fetches the details of a product by its ID.
Response:
Status: 200 OK
Body:
**{
    "id": 1,
    "name": "Product A",
    "price": 100.0,
    "st**ock_level": 50
}**

2. Update Product
Endpoint: /products/<id>/update
Method: PUT
Description: Updates the details of an existing product by its ID.
Request Body:
**{
    "name": "Updated Product Name",
    "price": 120.0,
    "stock_level": 40
}**
Response:
Status: 200 OK
Body:
**{
    "message": "Product updated"
}**
3. Delete Product
Endpoint: /products/<id>/delete
Method: DELETE
Description: Deletes a product from the database by its ID.
Response:
Status: 200 OK
Body:
**{
    "message": "Product deleted"
}**
