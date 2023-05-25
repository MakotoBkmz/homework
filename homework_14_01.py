user_input = int(input("Введите число (1, 2 или любое другое): "))
def anecdote(number):
    if number == 1:
        joke = "Анекдот про школу"
    elif number == 2:
        joke = "Анекдот про рибака"
    elif number != 1 or 2:
        joke = "Анекдот про кота"

    return joke

joke = anecdote(user_input)
print(joke)

