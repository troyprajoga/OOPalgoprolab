from car import Car
from electric_car import ElectricCar


def perform_driving_actions(vehicle):
    vehicle.accelerate()
    vehicle.brake()


car = Car("Mercedes", "GLC300")
electric_car = ElectricCar("Wuling", "EV", 75)

# encapsulating because class inside the car.py
car.accelerate()
car.brake()

# this is the inheritance
electric_car.accelerate()
electric_car.charge_battery()

# using perform_driving_action for car and electric car is polymorphism
perform_driving_actions(car)
perform_driving_actions(electric_car)

electric_car.start_engine()
