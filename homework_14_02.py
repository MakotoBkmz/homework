length = float(input('Введите длинну (только цифры): '))
width = float(input('Ввкдите ширину (только цифры): '))


def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return (perimeter)


perimeter = calculate_perimeter(length, width)
print('Периметр приямоугольника равен', perimeter)
