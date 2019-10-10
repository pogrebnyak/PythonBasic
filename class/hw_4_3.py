def text_stat(text,*filter):
    text_dict = {}
    for i in text:
        if text_dict.get(i) is not None:
            continue
        else:
            text_dict[i] = text.count(i)
            
    for i in filter:
        if text_dict.get(i) is None:
            continue
        del text_dict[i]

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
    exception_input = input('Введите исключения через пробел: ')
    exception_input = exception_input.lower().split()

    text_input = text_input.lower()
    text_list = text_input.split()
    words_stat = text_stat(text_list,*exception_input)
    # words_stat = text_stat(text_list)
    # words_stat = text_stat(text_list,'crew')
    # words_stat = text_stat(text_list,'were','crew')
    # words_stat = text_stat(text_list,'were','crew','two')
    print('')

    word_sorted = list(words_stat.keys())
    word_sorted.sort()

    for i in word_sorted:
        print(repr(i), '=', words_stat[i])
    print('')




