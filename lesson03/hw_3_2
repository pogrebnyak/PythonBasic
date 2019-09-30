def nok(a,b):
    if a > b:
      a,b = b,a
    for res in range(b,a*b+1):
      if res%a == 0 and res%b == 0:
          break
    return res

y = 'y'

while y == 'y':
  a = int(input('a: '))
  b = int(input('b: '))
  
  print(nok(a,b))        
  y = input('Еще раз?(y/n):')
