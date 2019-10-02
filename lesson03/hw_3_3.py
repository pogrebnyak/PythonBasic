import math

def input_value(str_value):
    while True:
        try:
            f = float(input(str_value + ': '))
            if f <= 0:
                print('Должно быть больше нуля' + '\n')
                continue
            break
        except ValueError:
            print('ОШИБКА! Вы должны ввести целое или вещественное число' + '\n')
    return f

def circle(r):  #КРУГ
  area_circle = math.pi * (r ** 2)
  return area_circle

def rect(a, b):  #ПРЯМОУГОЛЬНИК
  area = a * b
  perimeter = 2 * (a + b)
  return area, perimeter 

def triangle(a, b, c):  #ТРЕУГОЛЬНИК
    p = (a + b + c) / 2
    podkoren = p * (p - a) * (p - b) * (p - c)
    if podkoren < 0 or podkoren == 0:
        print('Такого треугольник не существует' + '\n')
        area = None
    else:
        area = math.sqrt(podkoren)
        return area

if __name__ == "__main__":

    menu_choice = ('1', '2', '3', '4')   
      
    while True:
        print("1. Расчитать площадь круга")
        print("2. Расчитать площадь треугольника по формуле Герона")
        print("3. Расчитать площадь и периметр прямоугольника")
        print("4. Выход")
        
        while True:
            y = input('Выберите (1, 2, 3, 4): ')
            if y not in menu_choice:
              print('ОШИБКА! Вы дожны выбрать из (1, 2, 3, 4)\n')
              continue
            break
        
        # Круг
        if y == '1':
            print(' ')
            radius_circle = input_value('Введите радиус круга')
            print('Площадь круга: ' + str(circle(radius_circle)) + '\n')
            
        # Треугольник
        elif y == '2':
            print(' ')
            while True:
              triangle_a = input_value('Введите сторону a')
              triangle_b = input_value('Введите сторону b')
              triangle_c = input_value('Введите сторону c')
              area_triangle = triangle(triangle_a, triangle_b, triangle_c)
              if area_triangle != None:
                  print('Площадь треугольника: ' + str(area_triangle) + '\n')
                  break
                
        # Прямоугольник
        elif y == '3':
            print(' ')
            rect_a = input_value('Введите длину прямоугольника')
            rect_b = input_value('Введите ширину прямоугольника')
            area_rect, perimeter_rect = rect(rect_a, rect_b)
            print('Площадь прямоугольника: ' + str(area_rect))
            print('Периметр прямоугольника: ' + str(perimeter_rect) + '\n')
            
        # Выход
        elif y == '4':
            print('Выход')
            break
