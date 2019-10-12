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

if __name__ == "__main__":
    text_input = ''
    lines = 0

    while True:
        text_s = input('Введите строку : ')
        text_input += f'{text_s} '
        if text_s == '':
            text_input = text_input[:-2]
            break
        lines += 1

    print(repr(text_input))

    text_input = text_input.lower()
    text_list = text_input.split()
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
