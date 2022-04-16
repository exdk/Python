import random

def is_valid(n): # Проверка на соответствие введенного значения условию
    return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100


def input_num(): # Ввод данных
    while True:
        number = input()
        if is_valid(number):
            return int(number)
        else:
            print('Число должно быть в диапазоне от 1 до 100')


def compare_num(first_num, second_num): # Сравнение введенного значения с загаданным
    num = random.randint(first_num, second_num)
    total = 0
    while True:
        n = input_num()
        total += 1
        if n < num:
            print('Не угадали, попробуйте число побольше')
        elif n > num:
            print('Не верно, назовите число поменьше')
        else:
            print('Ура! Вы угадали ответ за', total,  'попыток, поздравляем!' )
            break


def continue_game(): # Предложение продолжить игру
    answer = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if answer not in ('y', 'д', 'n', 'н'):
            answer = input('Ну что же Вы, нужно написать одну букву:\nПродолжим ("д"/"н")?\n')
        elif answer in ('n', 'н'):
            print('До новых встреч!')
            return False
        else:
            return True


def game(): # Запуск игры
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


game() # Вызов игры