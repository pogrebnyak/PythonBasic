def text_stat(text,filter = ''):
    text_dict = {}
    for i in text:
        if text_dict.get(i) is not None:
            continue
        else:
            text_dict[i] = text.count(i)
            
    filter = filter.lower().split()

    for i in filter:
        if text_dict.get(i) is None:
            continue
        del text_dict[i]

    return text_dict

while True:
    text_input = input('Введите строку : ')
    if text_input == '':
        break
    exception_input = input('Введите исключения через пробел: ')


    # text_input = '''About 90 percent of all children attend public school, which is free. The other 10 percent go I private schools,
    # which often include religious education. They are similar to the public schools but parents must pay for their children to go to
    # these schools. About half of all private schools are run by Catholics.'''

    # exception_input = ''
    # exception_input = 'of'
    # exception_input = 'of all'
    # exception_input = 'of all two'

    text_input = text_input.lower()
    text_list = text_input.split()
    words_stat = text_stat(text_list,exception_input)
    print('')

    word_sorted = list(words_stat.keys())
    word_sorted.sort()

    for i in word_sorted:
        print(repr(i), '=', words_stat[i])
    print('')
