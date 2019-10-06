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

    text_input = '''About 90 percent of all children attend public school, which is free. The other 10 percent go I private schools, 
        which often include religious education. They are similar to the public schools but parents must pay for their children to go to 
        these schools. About half of all private schools are run by Catholics.'''

    text_input = text_input.lower()
    text_list = text_input.split()
    lines = len(text_input.splitlines())
    digits = digit_count(text_input)
    words_stat = text_stat(text_list)
    chars_stat = text_stat(text_input)
    print('')
    print('Всего строк: '+str(lines)+'\n')

    print('Всего цифр: '+str(digits)+'\n')

    word_sorted = list(words_stat.keys())
    word_sorted.sort()

    for i in word_sorted:
        print(repr(i),'=',words_stat[i])
    print('')

    chars_sorted = list(chars_stat.keys())
    chars_sorted.sort()

    for i in chars_sorted:
        print(repr(i),'=',chars_stat[i])
