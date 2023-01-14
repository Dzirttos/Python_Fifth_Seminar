# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import os
os.system('cls')

print('Введите, пожалуйста, первое число.')
x = int(input())
print('Введите, пожалуйста, второе число.')
y = int(input())

def summary(a, b):
    if a == 0:
        return b
    elif a > 0:
        return summary(a - 1, b + 1)
    else:
        return summary(a + 1, b - 1)

print(f'\033[35mСумма числа {x} и числа {round(y)} равна {summary(x, y)}.')

