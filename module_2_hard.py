number = int(input('Введите число от 3 до 20: '))
password = []
for i in range(1, number):
    for j in range(2, number):
        flag = any(j == i for i in password)
        if flag:
            continue
        if number % (i + j) == 0 and i != j and (i or j) <= (number / 2):
            password.append(i)
            password.append(j)
        else:
            continue
print('Пароль: ', *password)
