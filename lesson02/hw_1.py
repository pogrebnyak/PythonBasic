print('''Игра \"СПИЧКИ\"
Правила: на столе лежат N спичек. Игроки по очереди берут на свой выбор 1,2 или 3 спички. 
Проиграет тот, кто возьмет последнюю.
''')
matches = ''
y = 'y'
name_player1 = input('Введите имя Игрока №1: ')
name_player2 = input('Введите имя Игрока №2: ')

while y == 'y':
    while True:
        matches = input('Введите количество спичек N: ')
        if not matches.isdigit():
            print('N не может быть строкой.')
            continue
        break
    matches = int(matches)
    print('На столе лежит спичек:', matches)
    while True:

        while True:
            choice_player1 = input(name_player1 + ', выберите количество спичек которые вы хотите убрать (1,2,3): ')
            if not choice_player1.isdigit():
                print('ОШИБКА! Не может быть строкой. Введите (1,2,3)')
                continue
            elif int(choice_player1) > 3 or int(choice_player1) == 0:
                print('ОШИБКА! Должно быть меньше 4. Введите (1,2,3)')
                continue
            elif int(choice_player1) > matches:
                print('ОШИБКА! Вы должны выбрать количество спичек не больше чем на столе')
                continue
            else:
                break

        matches -= int(choice_player1)
        if matches <= 0:
            print('Выиграл ' + name_player2)
            break
        else:
            print('На столе осталось спичек:', matches)

        while True:
            choice_player2 = input(name_player2 + ', выберите количество спичек которые вы хотите убрать (1,2,3): ')
            if not choice_player2.isdigit():
                print('ОШИБКА! Не может быть строкой. Введите (1,2,3)')
                continue
            elif int(choice_player2) > 3 or int(choice_player2) == 0:
                print('ОШИБКА! Должно быть меньше 4. Введите (1,2,3)')
                continue
            elif int(choice_player2) > matches:
                print('ОШИБКА! Вы должны выбрать количество спичей не больше чем на столе')
                continue
            else:
                break

        matches -= int(choice_player2)
        if matches <= 0:
            print('Выиграл ' + name_player1)
            break
        else:
            print('На столе осталось спичек:', matches)
    y = input('Хотите сыграть еще раз(y/n)? ')
