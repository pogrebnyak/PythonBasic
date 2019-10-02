def nok(a, b):
    if a > b:
      a, b = b, a
    for res in range(b, a * b + 1):
      if res % a == 0 and res % b == 0:
          break
    return res

def input_value(str_value):
    while True:
        try:
            f = int(input(str_value + ': '))
            if f <= 0:
                print('Должно быть больше нуля')
                continue
            break
        except ValueError:
            print('ОШИБКА! Вы должны ввести целое число')
    return f

if __name__ == "__main__":
    
    print('Программа выводит НОК двух чисел a и b')

    y = 'y'

    while y == 'y':
      input_a = input_value('Введите a')
      input_b = input_value('Введите b')
      
      print('НОК чисел ' + str(input_a) + ' и ' + str(input_b) + ': ' + str(nok(input_a, input_b)))
      y = input('Еще раз? (y/n): ')
