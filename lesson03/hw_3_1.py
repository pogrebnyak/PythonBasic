def calc(a):
  res = 0
  for i in str(a):
    if i.isdigit():
      res += 1
  return res


if __name__ == "__main__":

  print('Программа подсчета цифр в числе')
  y = 'y'
  while y == 'y':
    
    while True:
      global a
      try:
        input_value = int(input('Введите цело число: '))
        break
      except ValueError:
        print('ОШИБКА! Вы должны ввести целое число')

    print('В числе ' + str(input_value) + ' цифр : ' + str(calc(input_value)))
    y = input('Еще раз? (y/n): ')
