user_input = input('Введите первое слово: ')
user_input2 = input('Введите второе слово для удаления из первого: ')
def remove_letters(word, target_string):
    cleared_letters = ''
    target_string_lower = target_string.lower()
    for char in word:
        if char.lower() not in target_string_lower:
            cleared_letters += char
    return cleared_letters

removed_letters = remove_letters(user_input, user_input2)

print('Результа удаления:', removed_letters)