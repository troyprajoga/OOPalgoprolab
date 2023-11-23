from abc import ABC, abstractmethod

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0


    def accelerate(self):
        self.speed += 10
        print(f"The {self.make} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        self.speed -= 5
        print(f"The {self.make} {self.model} is braking. Current speed: {self.speed} km/h")

#getter
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

# setter
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    @abstractmethod
    def start_engine(ABC):
        pass
