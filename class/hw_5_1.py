class Car:

    cashbox = 0
    car_in = 0

    def __init__(self, vin, model, color, cost):
      self.vin = vin  
      self.model = model
      self.color = color
      self.cost = cost
      print('Добавлена машина {1} цвета {2}. Стоимостью {3}$ c VIN: {0}'.format(self.vin, self.model, self.color, self.cost))
      Car.car_in += 1
            

    def cashbox_info():
        print('Выручка: {}$'.format(Car.cashbox))

    def car_info(self):
       print('{} {} {} {}'.format(self.vin, self.model, self.color, self.cost))

    def how_many():
        print('У нас в гараже {} машин'.format(Car.car_in))

    def __del__(self):
        # продажа авто
        Car.car_in -= 1
        print('Продали {} за {}$'.format(self.model, self.cost))
        Car.cashbox += self.cost
        Car.cashbox_info()
        if Car.car_in == 0:
            print('Это была последняя машина')
        else:
            print('Осталось {} машин'.format(Car.car_in))

    def paint_car(self, color):
       color_old = self.color 
       self.color = color
       print('Машина {} перекрашена с цвета {} в цвет {} '.format(self.model, color_old, color))
       print('Стоимость услуги покраски 500$')
       Car.cashbox += 500
       Car.cashbox_info()
       

car1 = Car('123', 'Audi', 'red', 12000)
car2 = Car('321', 'BMW', 'blue', 15000)
car3 = Car('213', 'Mersedes', 'black', 17000)
car4 = Car('124', 'Opel', 'white', 13000)
car5 = Car('125', 'Ford', 'green', 11000)
cars = [car1, car2, car3, car4, car5]
Car.how_many()
Car.paint_car(car1, 'red')
Car.paint_car(car2, 'red')
Car.paint_car(car3, 'red')
Car.paint_car(car4, 'red')

del car1
del car2
del car3
del car4
Car.paint_car(car5, 'black')
del car5
