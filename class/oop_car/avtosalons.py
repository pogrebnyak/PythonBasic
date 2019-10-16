from .cars import Car


class Salon:

    def __init__(self, catalog, cash=0.0):
        """

        :param catalog: изменяемая коллекция объектов Car
        :param cash: float - выручка салона
        """
        self.catalog = catalog
        self.cash = cash

    def __str__(self):
        result = [f"Выручка = {self.cash}"]
        for i, car in enumerate(self.catalog, start=1):
            result.append(f"{i}. {str(car)}")
        return '\n'.join(result)

    def __repr__(self):
        result = [f"Выручка = {self.cash}"]
        for car in self.catalog:
            result.append(repr(car))
        return f"{self.__class__.__name__}(" \
               f"[{','.join(result)}], " \
               f"{self.cash}" \
               f")"

    def delivery(self, *cars, container=None):
        """
            Поставка

        Если поставка в виде партии машин, то наценка 30%
        Если поставка в виде контейнера, то наценка 40%

        :param cars: последовательность объектов Car
        :param container: последовательность объектов Car
        :return: None
        """
        for car in cars:
            self.append(car.name, car.color, int(car.price * 1.3))
        if container:
            for car in container:
                self.append(car.name, car.color, int(car.price * 1.4))

    def append(self, name, color, price):
        self.catalog.append(Car(name, color, price))

    def sail(self, name, color, price):
        """
            Продажа одного автомобиля

        :param name:
        :param color:
        :param price:
        :return:
        """
        # Найти порядковый номер автомобиля с подходящими параметратми в каталоге
        for i, car in enumerate(self.catalog):
            if (car.name, car.color, car.price) == (name, color, price):
                del self.catalog[i]  # удаляем элемент из списка, но не сам объект, ссылка на котроый хранится в car
                self.cash += car.price  # фиксируем выручку
                return car  # функция возвращает объект - автомобиль который был продан
        else:
            raise ValueError('Автомобиль не найден')

    def paint(self, car, color, price):
        """
            Услуга покраски автомобиля

        :param car: автомобиль, экземпляр класса Car
        :param color: в какой цвет покрасить
        :param price: цена покраски
        :return:
        """
        car.color = color  # краси
        self.cash += price  # пополняем кассу выручкой за услугу
