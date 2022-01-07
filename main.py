import vehicles
from vehicles.vehicles import Vehicle
from vehicles_types.types import VehicleType

if __name__ == '__main__':
    # # creating a new vehicle - have to provide: model name,  licence_number, available_energy, max_tire_pressure, current_tires_pressure,
    # # vehicle_type_id_number
    # car = Vehicle('seat arona', 41546546, 50, 75, 25, "61d77e364ace9457d9c2c34f")
    # # post new car to database
    # car.post_vehicle()
    # print(car.get_all_vehicles())
    # # get specific vehicle data by providing a licence number
    # data = Vehicle.get_vehicle_by_licence_number("3548523")
    # print(data)
    # # creat a new vehicle type
    # added_type = VehicleType("Truck")
    # # add the new type to the database
    # added_type.add_new_vehicle_type()
    # # get all vehicles types that are available in the garage database
    # current_try = VehicleType.get_all_vehicles_types()
    # print(current_try)
    data = Vehicle.refuel_a_vehicle_or_recharge('3548523')
    print(data)
