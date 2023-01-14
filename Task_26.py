import os
os.system('cls')


def power(a, b):
    if b == 0: return 1
    elif b >= 1:
        return a*power(a, b-1)


print(power(3, 2))
