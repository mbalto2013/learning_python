import sqlite3
from customer import Customer, customer_from_tuple
from weight import Weight, weight_from_tuple
from sqlite3 import Error


class Database:
    def __init__(self):
        self.db_name = 'weight_loss.db'

    def create_data_base(self):
        my_connection = None
        try:
            my_connection = sqlite3.connect(self.db_name)
            my_connection.cursor().execute('CREATE TABLE IF NOT EXISTS customer ('
                                           'ssn INTEGER PRIMARY KEY NOT NULL,'
                                           'name TEXT NOT NULL,'
                                           'last_name TEXT NOT NULL,'
                                           'day_of_birth TEXT NOT NULL,'
                                           'height FLOAT NOT NULL'
                                           ')')
            my_connection.cursor().execute('CREATE TABLE weight_loss ('
                                           'weight_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                           'ssn INTEGER,'
                                           'date_of_measurement TEXT NOT NULL,'
                                           'weight FLOAT NOT NULL,'
                                           'FOREIGN KEY(ssn) REFERENCES customer(ssn)'
                                           ')')
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close()

    def insert_customer(self, customer_data):
        total_changes = 0
        customer = Customer(customer_data)
        my_connection = None
        try:
            query = f'INSERT into customer VALUES(' \
                    f'{customer.ssn},' \
                    f'"{customer.name}",' \
                    f'"{customer.last_name}",' \
                    f'"{customer.day_of_birth}",' \
                    f'{customer.height}' \
                    f')'

            my_connection = sqlite3.connect(self.db_name)
            cursor = my_connection.cursor()
            cursor.execute(query)
            my_connection.commit()
            total_changes = my_connection.total_changes
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close()
            return {'changes': total_changes}

    def insert_weight(self, weigh_data):
        total_changes = 0
        user_weight = Weight(weigh_data)
        my_connection = None

        try:
            query = f'INSERT INTO weight_loss (ssn,date_of_measurement,weight)' \
                    f'VALUES(' \
                    f'{user_weight.ssn},' \
                    f' "{user_weight.date_of_measurement}",' \
                    f' {user_weight.weight}' \
                    f')'
            my_connection = sqlite3.connect(self.db_name)
            cursor = my_connection.cursor()
            cursor.execute(query)
            my_connection.commit()
            total_changes = my_connection.total_changes
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close()
            return {'changes': total_changes}

    def weight_history_by_user(self, customer_ssn):
        my_connection = None
        weight_history = {}

        try:
            query = f'SELECT DISTINCT ssn,date_of_measurement, weight  ' \
                    f'FROM weight_loss ' \
                    f'WHERE ssn={customer_ssn} ' \
                    f'ORDER by date_of_measurement ASC, weight DESC '
            my_connection = sqlite3.connect(self.db_name)
            cursor = my_connection.cursor()
            customer_data = cursor.execute(query).fetchall()
            weight_history['weight_history'] = [
                weight_from_tuple(entry).info() for entry in customer_data]
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close
                return weight_history

    def customer_info(self, customer_ssn):
        my_connection = None
        customer_data = {}
        try:
            query = f'SELECT * FROM customer'
            my_connection = sqlite3.connect(self.db_name)
            cursor = my_connection.cursor()
            customer_data = customer_from_tuple(
                cursor.execute(query).fetchone()).info()
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close()
                return customer_data

    def customers(self):
        my_connection = None
        customers = {'customers': None}
        try:
            query = f'SELECT * FROM customer'
            my_connection = sqlite3.connect(self.db_name)
            cursor = my_connection.cursor()
            customer_data = cursor.execute(query).fetchall()
            customers['customers'] = [customer_from_tuple(
                customer).info() for customer in customer_data]
        except Error as e:
            print(e)
        finally:
            if my_connection:
                my_connection.close()
                return customers
