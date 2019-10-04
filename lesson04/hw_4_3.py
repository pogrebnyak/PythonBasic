def text_stat(text,excep = ''):
    text_dict = {}
    for i in text:
        if text_dict.get(i) is not None:
            continue
        else:
            text_dict[i] = text.count(i)
    excep = excep.lower()
    excep = excep.split()

    for i in excep:
        if text_dict.get(i) is None:
            continue
        del text_dict[i]

    return text_dict

while True:
    text_input = input('Введите строку : ')
    exception_input = input('Введите слово или слова которые не нужно считать: ')
    if text_input == '':
        break

    text_input = text_input.lower()
    text_list = text_input.split()
    words_stat = text_stat(text_list,exception_input)
    print('')

    word_sorted = list(words_stat.keys())
    word_sorted.sort()

    for i in word_sorted:
        print(repr(i), '=', words_stat[i])
    print('')
