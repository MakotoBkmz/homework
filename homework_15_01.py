miles = float(input("Введите количество миль: "))

def miles_kilometers(miles):
    if miles < 0:
        raise ValueError("Отрицательное число!")
    else:
        kilometers = miles * 1.60934
        return kilometers.__round__(1)
try:
    kilometers = miles_kilometers(miles)
    print(f"{miles} миль = {kilometers} километров")
except ValueError as error:
    print(error)