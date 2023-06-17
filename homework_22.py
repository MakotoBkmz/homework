from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, fuel_capacity, fuel_level, speed, mileage):
        self.brand = brand
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.speed = speed
        self.mileage = mileage

    @abstractmethod
    def __str__(self):
        pass

    def refuel(self, amount):
        self.fuel_level = min(self.fuel_level + amount, self.fuel_capacity)

    def transfer_fuel(self, other_vehicle, amount):
        available_space = other_vehicle.fuel_capacity - other_vehicle.fuel_level
        fuel_to_transfer = min(amount, available_space, self.fuel_level)
        self.fuel_level -= fuel_to_transfer
        other_vehicle.fuel_level += fuel_to_transfer


class Car(Vehicle):
    def __init__(self, brand, fuel_capacity, fuel_level, speed, mileage, passenger_count, has_airbags):
        super().__init__(brand, fuel_capacity, fuel_level, speed, mileage)
        self.passenger_count = passenger_count
        self.has_airbags = has_airbags

    def __str__(self):
        return f"Car: {self.brand}, Fuel Level: {self.fuel_level}, Mileage: {self.mileage}"

    def __repr__(self):
        return str(self)


class Motorcycle(Vehicle):
    def __init__(self, brand, fuel_capacity, fuel_level, speed, mileage, has_sidecar):
        super().__init__(brand, fuel_capacity, fuel_level, speed, mileage)
        self.has_sidecar = has_sidecar

    def __str__(self):
        return f"Motorcycle: {self.brand}, Fuel Level: {self.fuel_level}, Mileage: {self.mileage}"

    def __repr__(self):
        return str(self)


car = Car("Toyota", 60, 20, 120, 5000, 4, True)
motorcycle = Motorcycle("Harley-Davidson", 20, 10, 100, 3000, True)

print(car)
print(motorcycle)

car.refuel(10)
print("Car fuel level after refueling", car.fuel_level)

car.transfer_fuel(motorcycle, 15)
print("Car fuel level", car.fuel_level)
print("Bike fuel level", motorcycle.fuel_level)
