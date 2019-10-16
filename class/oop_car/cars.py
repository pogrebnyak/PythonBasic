class Car(object):
    """
    self.price - чистая цена. Может быть изменена методом  "Акция"
    self.skidka - по-умолчанию отсутсвует. Создаётся методом "Акция"
    """

    def __init__(self, name, color, price):
        self.name = name
        if not isinstance(color, str):
            raise ValueError('color incorrect type')
        self.color = color

        if not isinstance(price, int):
            raise ValueError('price incorrect type')
        self.price = price

    def __str__(self):
        return f"{self.name} цвета {self.color} по цене {self.price}"

    def __repr__(self):
        return f"Car({repr(self.name)}, {repr(self.color)}, {repr(self.price)})"


class SportCar(Car):
    pass
