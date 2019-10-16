from oop_car import Car, Salon


salon = Salon([
    Car('Mazda 3', 'magenta', 15000),
    Car('Nissan Almera', 'red', 12000),
    Car('Opel Astra', 'white', 11000),
    Car('Toyota LandCruiser', 'black', 110000),
])

print('-' * 60)
print('Начальное состояние салона:')
print(salon)
print('-' * 60)
print(repr(salon))

print('-' * 60)
car = salon.sail('Mazda 3', 'magenta', 15000)
print(f"Продали {car.name}({car.color}, {car.price})")
print('Состояние салона:')
print(salon)

print('-' * 60)
car = salon.sail('Opel Astra', 'white', 11000)
print(f"Продали {car.name}({car.color}, {car.price})")
salon.paint(car, 'yelow', 220)
print(f"Перекрасили {car.name}({car.color}, {car.price})")
print('Состояние салона:')
print(salon)

print('-' * 60)
print('Новая комплексная поставка!')
print('Партия машин:')
cars = (
    Car('Mazda 3', 'cyan', 10000),
    Car('Nissan Almera', 'red', 9000),
    Car('Opel Astra', 'red', 11000),
    Car('Toyota LandCruiser', 'cream', 90000),
)
for car in cars:
    print(f"\t{str(car)}")
print('Контейнер с машинами:')
car_container = (
    Car('Mazda 3', 'cyan', 9000),
    Car('Nissan Almera', 'red', 8500),
    Car('Opel Astra', 'red', 10000),
    Car('Toyota LandCruiser', 'cream', 81000),
)
for car in car_container:
    print(f"\t{str(car)}")
salon.delivery(*cars, container=car_container)
print('Состояние салона:')
print(salon)

"""
Что дальше?

Класс Salon:
===========
* Выгрузка в файл и загрузка из файла данных салона в методах open() и close()
* Ведение журнала поступлений и продаж
* Получение даннх о контейнерной поставке из внешнего текстового файла

Новый класс для автосалона на основе Salon, в котором будут изменения и дополнения функциональности:
===================================================================================================
* Название салона
* Ввести понятие ID автомобиля в каталоге
    * обеспечить уникальность ID на протяжении всей жизни салона
        * вариант атрибута с автоинкрементом
        * вариант UUID (https://ru.wikipedia.org/wiki/UUID)
    * написать скрипт конвертации файла с данными салона
    * добавить функциональность выбора автомобиля по его ID из каталога 

Программа:
=========
* Разработать класс сценария работы салона
* Сохранение данных сценария в текстовом виде в файл
* Выполнение файла сценария
"""
