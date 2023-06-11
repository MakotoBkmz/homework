import datetime

class Vehicle:
    def __init__(self, manufacturer, model, fuel_consumption, year=2020, mileage=0):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"Vehicle: {self.manufacturer} {self.model}, {self.year} release date"

    @property
    def age(self):
        current_year = datetime.datetime.today().year
        return current_year - self.year


car1 = Vehicle("Tesla", "S-Class", 7.5, 2019, 50000)
car2 = Vehicle("Subaru", "Legacy", 9.2, 2017, 80000)
car3 = Vehicle("Honda", "Prelude", 6.8, 2003, 120000)
car4 = Vehicle("Mercedes", "Roadster Z3", 8.4, 2005, 98000)
car5 = Vehicle("Mercedes", "Roadster Z3", 8.4)

print(car1, f"Vehicle age 1: {car1.age} years")
print(car2, f"Vehicle age 2: {car2.age} years")
print(car3, f"Vehicle age 3: {car3.age} years")
print(car4, f"Vehicle age 3: {car4.age} years")
print(car5, f"Vehicle age 3: {car5.age} years")