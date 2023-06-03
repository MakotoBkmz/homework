user_input = int(input('Введите положительное число: '))

def generate_list(start_value):
    if start_value <= 0:
        raise ValueError("Число должно быть положительным!")

    return [start_value + digit for digit in range(10)]

try:
    result = generate_list(user_input)
    print(result)
except ValueError as error:
    print(error)