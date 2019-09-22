import math

while True:
  print('Вычисление площади треуголника по формуле Герона')
  while True:
    a=input('Введите длину стороны a (мм): ')
    if a.isdigit() == 0 :
        print('ОШИБКА! Длина стороны a должена быть целое цисло больше нуля')
        continue
    if int(a) == 0 :
        print('ОШИБКА! Длина стороны a не может равняться нулю')
        continue
    a=int(a)
    break
  while True:
    b = input('Введите длину стороны b (мм) : ')
    if b.isdigit() == 0 :
        print('ОШИБКА! Длина стороны b должена быть целое цисло больше нуля')
        continue
    if int(b) == 0 :
        print('ОШИБКА! Длина стороны b не может равняться нулю')
        continue
    b = int( b )
    break
  while True:
    c = input('Введите длину стороны c (мм) : ')
    if c.isdigit() == 0 :
        print('ОШИБКА! Длина стороны c должена быть целое цисло больше нуля')
        continue
    if int(c) == 0 :
        print('ОШИБКА! Длина стороны c не может равняться нулю')
        continue
    c=int(c)
    break
  p=(a + b + c) / 2
  podkoren = p * (p - a) * (p - b) * (p - c)
  if podkoren < 0 or podkoren == 0 :
      print('Такого треугольник не существует')
      continue
  S = round(math.sqrt(podkoren),4)
  print('Площадь треугольника = ', S, 'мм' +u'\u00b2')
  y = input('Вычислить площадь треугольника еще раз (y/n)? ')
  if y != 'y': break
