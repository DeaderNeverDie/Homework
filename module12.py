#import random
#
# print('Задача 1. Сумма чисел')
# def summa_n():
#     number = int(input('Введите число: '))
#     countSumm = 0
#     for x in range(1, number + 1):
#         countSumm += x
#     print(f'Сумма чисел от 1 до {number} равна {countSumm}')
#
# summa_n()

# print('Задача 2. Функция в функции')
# def test():
#     number = int(input('Введите число: '))
#     if number > 0:
#         positive()
#         test()
#     elif number < 0:
#         negative()
#         test()
#     else:
#         print('Число равно нулю. Введите другое число.')
#         test()
#
# def positive():
#     print('Положительное')
#     test()
# def negative():
#     print('Отрицательное')
#     test()
#
# test()

print('Задача 3. Апгрейд калькулятора')
def menu():
    number = int(input('Введите число: '))
    choice = int(input(f'Введите номер действия:'
                       f'\n1 - сумма цифр'
                       f'\n2 - максимальная цифра'
                       f'\n3 - минимальная цифра:'))
    if choice == 1:
        count_summ(number)
    elif choice == 2:
        max_number(number)
    elif choice == 3:
        min_number(number)
    else:
        print('Ошибка ввода. Попробуйте ещё раз')
        menu()
def count_summ(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    print(f'Сумма цифр: {summ}')
    menu()
def max_number(number):
    print('Максимальная цифра:',max(str(number)))
    menu()
def min_number(number):
    print('Минимальная цифра:', min(str(number)))
    menu()

menu()

# print('Задача 4. Текстовый редактор')
# def count_letters():
#     text = list(str(input('Введите текст:')))
#     number = str(input('Какую цифру ищем?'))
#     letter = str(input('Какую букву ищем?'))
#     number_counter = 0
#     letter_counter = 0
#     for i in text:
#         if i == number:
#             number_counter +=1
#         elif i == letter:
#             letter_counter +=1
#     print(f'Количество цифр {number}: {number_counter}')
#     print(f'Количество букв {letter}: {letter_counter}')
# count_letters()


# print('Задача 5. Недоделка')
#
#
# def rock_paper_scissors():
#     choices = ['камень', 'ножницы', 'бумага']
#
#     while True:
#         player_choice = input('Выберите: камень, ножницы или бумага: ').lower()
#         if player_choice in choices:
#             break
#         else:
#             print('Некорректный ввод. Пожалуйста, выберите из: камень, ножницы или бумага.')
#
#     computer_choice = random.choice(choices)
#     print(f'Компьютер выбрал: {computer_choice}')
#
#     if player_choice == computer_choice:
#         print('Ничья!')
#     elif (
#         (player_choice == 'камень' and computer_choice == 'ножницы') or
#         (player_choice == 'ножницы' and computer_choice == 'бумага') or
#         (player_choice == 'бумага' and computer_choice == 'камень')):
#         print('Вы победили!')
#     else:
#         print('Вы проиграли!')
#
# def guess_the_number():
#     secret_number = random.randint(0, 10)
#     while True:
#         player_choice = int(input('Угадайте число от 0 до 10: '))
#         if player_choice < 0 or player_choice > 10:
#             print('Ошибка ввода. Пожалуйста, введите число от 0 до 10')
#             continue
#         elif player_choice != secret_number:
#                 print('Не отгадали')
#                 continue
#         else:
#             print('Вы победили')
#             break
#
#
# def main_menu():
#     game_choice = int(input('Выберите игру:'
#                             '\n1 - Камень, ножницы, бумага '
#                             '\n2 - Угадай число'
#                             '\n:'))
#     if game_choice == 1:
#         rock_paper_scissors()
#     elif game_choice == 2:
#         guess_the_number()
#     else:
#         print('Ошибка ввода.')
#         main_menu()
#
#
# main_menu()


