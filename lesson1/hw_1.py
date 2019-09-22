while True:
  print('Вычисление площади и периметра прямоугольника со сторонами A и B')
  while True:
      a = input("Введите длину А (мм): ")
      if a.isdigit() == 0 :
        print('ОШИБКА! Длина А должена быть целое цисло больше нуля')
        continue
      if int(a) == 0 :
        print('ОШИБКА! Длина А не может равняться нулю')
        continue
      break
  while True:
      b = input("Введите ширину B (мм): ")
      if b.isdigit() == 0 :
        print('ОШИБКА! Ширина B должена быть целое цисло больше нуля')
        continue
      if int(b) == 0 :
        print('ОШИБКА! Ширина B не может равняться нулю')
        continue
      break 
  
  S=int(a)*int(b)
  P=2*(int(a)+int(b))
  print("Площадь прямоугольник "+a+' мм x '+b+" мм =",S,'мм'+u"\u00b2")
  print("Периметр прямоугольника "+a+' мм x '+b+" мм =",P,'мм')
  y = input('Вычислить площать прямоугольника еще раз (y/n)? ')
  if y != 'y' : break
