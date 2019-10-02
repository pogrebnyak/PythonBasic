def calc(a):
    res = 0
    for i in a:
      if i.isdigit():
          res += 1
          
    return res

if __name__ == "__main__":

    print('Программа подсчета цифр в числе(int, float, complex)')
    y = 'y'

    while y == 'y':
      while True:
          s = 0
          input_value = (input('Введите цисло: '))
          try:
            input_value_complex = complex(input_value)
            break
          except ValueError:
            s = None
            break       
        
      if s is not None:
        print(calc(input_value))
      else:
        print(s) 
        break
      y = input('Еще раз?(y/n):')
