import math
# Задача 1. Конвертация
# euro = float(input('Стоимость покупки в евро: '))
# dollar = euro * 1.25
# ruble = dollar * 60.87
# print('Стоимость в рублях: ', ruble)
#
# Задача 2. Грубая математика
# replay = int(input('Введите кол-во чисел: '))
# for i in range(replay):
#     number = float(input('Введите число: '))
#     if number < 0:
#         number = math.floor(number)
#         exp_number = math.exp(number)
#         print('x = ', number, exp_number)
#     elif number > 0:
#         number = math.ceil(number)
#         log_number = math.log(number)
#         print('x = ', number, log_number)
#     else:
#         print(0)
#
# Задача 3. Аналог Steam
# size = float(input('Укажите размер файла для скачивания: '))
# speed  = float(input('Какова скорость вашего соединения: '))
# percent = int((round((speed / size),2)) * 100)
# percent_now = percent
# download = 0
# time = math.ceil(size / speed)
# for i in range(1,time + 1):
#     second = i
#     download += speed
#     if second == time:
#         print(f'Прошло {second} секунд. Скачано {size} из {size}.(100%)')
#     else:
#         print(f'Прошло {second} секунд. Скачано {download} из {size}.({percent}%)')
#     percent += percent_now


#Задача 4. Первая цифра
# number = float(input('Введите число: '))
# x = int(number)
# y = number - x
# after_point = int(y * 10)
# print(after_point)



# Задача 5. Вот это объёмы!
random_radius = float(input('Введите радиус случайной планеты: '))
earth_volume = 1.08321 * (10 ** 12)
random_volume = 4/3*3.141592653*(random_radius**3)
if earth_volume > random_volume:
    diff = round(earth_volume / random_volume, 3)
    print(f'Объём планеты Земля больше в {diff} раз')
else:
    diff = round(1 / round(earth_volume / random_volume, 3), 3)
    print(f'Объём планеты Земля меньше в {diff} раз')






