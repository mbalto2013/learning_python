import json
from flask import Flask, request
from database import Database

app = Flask(__name__)

my_database = Database()
my_database.create_data_base()


@app.route('/customer', methods=['POST'])
def insert_customer():
    data = request.get_json()
    return my_database.insert_customer(data)


@app.route('/weight', methods=['POST'])
def insert_weight():
    data = request.get_json()
    return my_database.insert_weight(data)


@app.route('/customer/weight_history_by_user/<ssn>', methods=['GET'])
def weight_history_by_use(ssn):
    return my_database.weight_history_by_user(ssn)


@app.route('/customer/<ssn>', methods=['GET'])
def customer_info(ssn):
    return my_database.customer_info(ssn)


@app.route('/customers/', methods=['GET'])
def customers():
    return my_database.customers()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
