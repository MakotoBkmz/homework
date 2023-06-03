def get_month():
    month = [
        "Январь",
        "Февраль",
        "Март",
        "Аппель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь"
    ]
    while True:
        for element in month:
            yield element

generator = get_month()
for month in generator:
    print(month)