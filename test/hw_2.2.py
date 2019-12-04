import math

summa=0

print("""Пользователь вводит два любых числа.
Выдать список всех натуральных чисел между этими двумя числами.""")

a = float(input('a: '))
b = float(input('b: '))
if a > b:
    a, b = b, a

a = int(a)
b = math.ceil(b)  # округляет в большую сторону. (int)

c = [i for i in range(a + 1, b) if i > 0]

print(c)

for i in c:
    summa+=int(i)

print(summa)

