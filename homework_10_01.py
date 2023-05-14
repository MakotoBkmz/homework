visited_cities = set(input("Введите города которые вы посетили за последние 10 лет >>> ").title().split())
planned_cities = set(input("Введите города которые вы хотели бы посетить в слудующие 10 лет: ").title().split())
favorite_cities = visited_cities.intersection(planned_cities)
if favorite_cities:
    print('Вам понравились ', favorite_cities)
else:
    print('Вы открыты к чему то новому!')

