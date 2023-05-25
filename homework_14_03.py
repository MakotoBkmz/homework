user_input = input('Введите слово, содержащее Ё, ё, Ж, ж: ')

def remove_letters(word):
    cleared_letters = ''
    for char in word:
        if char != 'ё' and char != 'Ё' and char != 'ж' and char != 'Ж':
            cleared_letters += char
    return cleared_letters

removed_letters = remove_letters(user_input)
print('Слово без Ё и Ж:', removed_letters)