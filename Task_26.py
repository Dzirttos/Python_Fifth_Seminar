# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

print('Какое число нужно возвести в степень?')
x = float(input())
print('А в какую степень нужно возвести?')
y = float(input())


def power(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / a * power(a, b+1)
    elif b >= 1:
        return a * power(a, b-1)


print(f'\033[32mЕсли число {round(x)} возвести в степень {round(y)},то получится {power(x, y)}.')


