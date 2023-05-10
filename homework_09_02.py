student_surnames = input("Введите фамилии раздельно >>> ").title()
for names in student_surnames:
     student_list = student_surnames.split()
     student_list.sort()
print ('Фамилии в алфавитном порядке >>>  ', student_list)