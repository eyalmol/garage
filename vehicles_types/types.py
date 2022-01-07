import requests

URL = 'http://localhost:4500/garage/vehiclesType'


class VehicleType:
    url = URL

    # initialize new vehicle type
    def __init__(self, name):
        self.name = name

    def add_new_vehicle_type(self):
        # set the data for the post request
        data = {"type": self.name}
        response = requests.post(self.url, json=data)
        if response.status_code == 200 or response.status_code == 201:
            return response.text
        else:
            return 'was not able to create/generate new vehicle type'

    @staticmethod
    def get_all_vehicles_types():
        response = requests.get(URL)
        return response.text