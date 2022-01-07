import requests


class Vehicle:
    type_exist = 'false'
    vehicle_collection_url = 'http://localhost:4500/garage/vehicles'
    posted = 'false'

    # initialize new car
    def __init__(self, model_name, licence_number, available_energy, max_tire_pressure, current_tires_pressure,
                 vehicle_type_id_number):
        self.name = model_name
        self.licence_number = licence_number
        self.available_energy = available_energy
        self.max_tire_pressure = max_tire_pressure
        self.current_tires_pressure = current_tires_pressure
        url = 'http://localhost:4500/garage/vehiclesType'
        response = requests.get(url)
        text = response.text
        # we only want to add new car if one has current number of vehicle type that is in the database
        if vehicle_type_id_number in text:
            self.vehicle_type_id_number = vehicle_type_id_number
            self.type_exist = 'true'
        else:
            print("type is not in the vehicles type collection, need to add type to vehicle type")

    def post_vehicle(self):
        if self.type_exist == 'true':
            # setting the data before publishing to database
            data = {'modelName': self.name, "licenceNumber": self.licence_number,
                    'availableEnergyPercentage': self.available_energy, 'maxTirePressure': self.max_tire_pressure,
                    'currentTirePressure': self.current_tires_pressure, 'type': self.vehicle_type_id_number}
            # setting response to the post request response
            response = requests.post(self.vehicle_collection_url, json=data)
            # check if the car has been published
            if response.status_code == 200:
                self.posted = 'true'
                return response.status_code
            else:
                return 'was not able posting to database'
        else:
            return 'type is not in the vehicles type collection'

    # by sending the server the url with get request we will get all the vehicles in the database
    def get_all_vehicles(self):
        response = requests.get(self.vehicle_collection_url)
        return response.text

    @staticmethod
    def get_vehicle_by_licence_number(licence_number):
        # by getting licence number, get specific car from database
        licence_url = 'http://localhost:4500/garage/vehicles' + '?licenceNumber=' + licence_number
        response = requests.get(licence_url)
        # check the response status code, if properly done send the vehicle as response
        if response.status_code == 200 or response.status_code == 201:
            return response.text
        else:
            return 'was not able to get vehicle by licence number'

    def inflate_tires_pressure_to_max(self, vehicle_id):
        # inflate tires to max pressure, sending the cars id as it defines in the database and the car max tire pressure with the intent
        inflate_tire_url = 'http://localhost:4500/garage/vehicles/' + vehicle_id + '/' + self.max_tire_pressure + '/inflateTire'
        response = requests.put(inflate_tire_url)
        if response.status_code == 200 or response.status_code == 201:
            return 'tires pressure change to max'
        else:
            return 'something went wrong in thr inflating tires method'

    @staticmethod
    def refuel_a_vehicle_or_recharge(licence_number):
        # set car by providing licence number energy/fuel to 100%
        add_energy_url = 'http://localhost:4500/garage/vehicles/' + licence_number + '/addEnergy'
        response = requests.put(add_energy_url)
        if response.status_code == 200 or response.status_code == 201:
            return response.text
        else:
            return 'could not refuel/charge energy'

