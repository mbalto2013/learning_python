from datetime import date, datetime


class Weight:
    weight_data: dict

    def __init__(self, weight_data):
        self.ssn = weight_data.get('ssn')
        self.date_of_measurement = weight_data.get('date_of_measurement')
        self.weight = weight_data.get('weight')

    def info(self):
        data = dict(ssn=self.ssn,
                    date_of_measurement=self.date_of_measurement,
                    weight=self.weight)
        return data


def weight_from_tuple(weight_values):
    weight_keys = ['ssn', 'date_of_measurement', 'weight']
    weight_dict = dict(zip(weight_keys, weight_values))
    return Weight(weight_dict)
