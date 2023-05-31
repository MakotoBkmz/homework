def sort_numbers(collection):
    sorted_set = sorted(set(collection))

    if isinstance(collection, dict):
        sorted_set = tuple(sorted_set.keys())
    return tuple(sorted_set)

numbers_set = set()

for _ in range(7):
    number = input("Введите семь однозначных чисел (от 0 до 9): ")
    try:
        number = int(number)
        if 0 <= number <= 9:
            numbers_set.add(number)
        else:
            print("Однозначное число! (0-9).")
    except ValueError:
        print("Вы не ввели число.")

result = sort_numbers(numbers_set)
print(result)
