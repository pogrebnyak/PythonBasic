print("""Пользователь вводит два любых числа.
Выдать список всех натуральных чисел между этими двумя числами.""")

import math

a = float(input('a: '))
b = float(input('b: '))
a = math.ceil(a)  #округляет в большую сторону. (int)
b = math.ceil(b)  #округляет в большую сторону. (int)
if a > b:
    a, b = b, a
       
c = [i for i in range(a,b) if i > 0]   

print(c)
