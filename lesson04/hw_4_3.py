def text_stat(text, *filter):
    if filter != ():
        if type(filter[0]) == tuple:
            filter = filter[0]

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

    exception_input = input('Введите исключения через пробел: ')
    exception_input = tuple(exception_input.lower().split())

    text_input = text_input.lower()
    text_list = text_input.split()
    words_stat = text_stat(text_list,exception_input)
    # words_stat = text_stat(text_list)
    # words_stat = text_stat(text_list, 'of')
    # words_stat = text_stat(text_list, 'of', 'all')
    # words_stat = text_stat(text_list, 'of', 'all', 'two')
    print('')

    word_sorted = list(words_stat.keys())
    word_sorted.sort()

    for i in word_sorted:
        print(repr(i), '=', words_stat[i])