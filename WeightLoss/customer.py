from typing import Dict, Any


class Customer:
    customer_data: dict

    def __init__(self, customer_data):
        self.ssn = customer_data.get('ssn')
        self.name = customer_data.get('name')
        self.last_name = customer_data.get('last_name')
        self.day_of_birth = customer_data.get('day_of_birth')
        self.height = customer_data.get('height')

    def info(self):
        data = dict(ssn=self.ssn,
                    name=self.name,
                    last_name=self.last_name,
                    day_of_birth=self.day_of_birth,
                    height=self.height)
        return data


def customer_from_tuple(customer_values):
    customer_keys = ['ssn', 'name', 'last_name', 'day_of_birth', 'height']
    customer_dict = dict(zip(customer_keys, customer_values))
    return Customer(customer_dict)
