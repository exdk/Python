import random

#задаем параметры для пароля
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
chars = ''

#запрашиваем параметры для пароля у пользователя
length = int(input('Какой длины нужен пароль?'))
digit = input('Нужны ли цифры в пароле (y/n)?')
ABC = input('Нужны ли ПРОПИСНЫЕ буквы (y/n)?')
abc = input('Нужны ли строчные буквы (y/n)?')
symbol = input('Добавить символы !#$%&*+-=?@^_ (y/n)?')

#соединяем хотелки пользователя
if digit == 'y':
    chars += digits
if ABC == 'y':
    chars += uppercase_letters
if abc == 'y':
    chars += lowercase_letters
if symbol == 'y':
    chars += punctuation

#функция генерации пароля
def generate_password(length, chars):
    pswrd = []
    pswrd.append(''.join(random.sample(chars, length)))
    print(*pswrd, end='')
    
#показываем пароль
generate_password(length, chars)