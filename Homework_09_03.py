user_input = input('Enter upper/lowercase letters, numbers, symbols  ')
upper_chars = ''
for char in user_input:
    if char.isupper():
        upper_chars += char
print('Uppercase characters:', upper_chars)
