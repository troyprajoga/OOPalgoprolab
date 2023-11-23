from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"Charging the battery of {self.make} {self.model} with a capacity of {self.battery_capacity} kWh.")


    def start_engine(ABC):
        print("ENGINEEEEEEEEEEEEEE")