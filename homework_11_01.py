import pprint

student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
student_name = input("Введіть ім'я та прізвище студента: ").title()
student_email = input("Введіть електронну пошту студента: ")
student_age = int(input("Введіть вік студента: "))
student_phone = input("Введіть номер телефону студента: ")
average_score = float(input("Введіть середній бал студента: "))

student[student_name] = {
    'Пошта': student_email,
    'Вік': student_age,
    'Номер телефону': student_phone,
    'Середній бал': average_score
}

for info in student.values():
    if info['Номер телефону'] is None:
        info['Номер телефону'] = input("Введіть номер батьків: ")

pprint.pprint(student)

print("Список студентів з середнім балом більше 90:")
for student_name, info in student.items():
    if info['Середній бал'] > 90:
        print(f"Ім'я та прізвище: {student_name} \nСередній бал: {info['Середній бал']}")

total_students = len(student)

total_score = sum(info['Середній бал'] for info in student.values())
average_score = total_score / total_students
print("Средний бал студентов:", average_score)
