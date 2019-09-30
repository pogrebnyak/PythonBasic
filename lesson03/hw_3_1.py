y = 'y'

while y == 'y':
  def calc(a):
    res = 0
    for i in str(a):
        res += 1
    if a<0 :
        res -= 1
    return res

  while True:
    global a
    try:
      input_value = int(input('a: '))
      break
    except ValueError:
      print('Введите целое число')

  print(calc(input_value))
  y = input('Еще раз?(y/n):')
