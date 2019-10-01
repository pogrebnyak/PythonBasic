y = 'y'

print('Программа подсчета цифр в числе')

while y == 'y':
  def calc(a):
    res = 0
    for i in str(a):
        if i.isdigit():
          res += 1
    return res

  while True:
    global a
    try:
      input_value = int(input('Введите цело число: '))
      break
    except ValueError:
      print('ОШИБКА! Вы должны ввести целое число')

  print('В числе ' + str(input_value) + ' цифр : ' + str(calc(input_value)))
  y = input('Еще раз? (y/n): ')
