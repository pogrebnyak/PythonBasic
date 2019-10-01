y = 'y'

def calc(a):
    res = 0
    for i in a:
      if i.isdigit():
          res += 1
          
    return res

while y == 'y':
  while True:
      s = 0
      input_value = (input('a: '))
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
