def text_stat(text):
  text_dict = {}
  for i in text:
     if text_dict.get(i) is not None:
         continue
     else:
         text_dict[i] = text.count(i)

  return text_dict

def digit_count(text):
  s = 0
  for i in text:
      if i.isdigit():
          s += 1
  return s

while True:
    text_input = input('Введите строку : ')
    if text_input == '':
        break

    text_input = text_input.lower()
    text_list = text_input.split()
    lines = len(text_input.splitlines())
    digits = digit_count(text_input)
    words_stat = text_stat(text_list)
    chars_stat = text_stat(text_input)
    print('')
    print('Всего строк: '+str(lines)+'\n')
    print('Всего цифр: '+str(digits)+'\n')

    for i,j in words_stat.items():
        print(repr(i),'=',j)
    print('')

    for i,j in chars_stat.items():
        print(repr(i),'=',j)

    print()
