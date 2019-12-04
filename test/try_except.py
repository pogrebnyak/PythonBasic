try:
    a=int(input('a: '))
    b=int(input('b: '))
    print(a/b)
except ZeroDivisionError:
    print('Division by Zero')
except Exception:
    print('All')