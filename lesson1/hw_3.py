import math

while True:
  print('Вычисление площади круга с радиусом R')
  while True:
    R = input('Введите радиус круга R (мм): ')
    if R.isdigit() == 0 :
        print('ОШИБКА! R должен быть целое цисло больше нуля')
        continue
    if int(R) == 0 :
        print('ОШИБКА! R не может равняться нулю')
        continue
    break
  S = round(math.pi*(int(R)**2),4)
  print('Площадь круг c радиусом '+R+' мм = ',S,'мм' +u'\u00b2')
  y = input('Вычислить площать прямоугольника еще раз (y/n)? ')
  if y != 'y' : break