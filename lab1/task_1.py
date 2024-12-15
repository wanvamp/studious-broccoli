# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
class Triangle():
    #Класс, представляющий невырожденные треугольники с определенными сторонами, выраженными натуральными числами
    def __init__(self, a: int, b: int, c: int):

        """
        Инициализирует экземпляр класса Triangle
        :param a: сторона а
        :param b: сторона b
        :param c: сторона c

        example:
        >>> triangle1 = Triangle(3, 4, 5)
        """

        #Проверка что стороны a, b, c - целые числа
        if not all(isinstance(i, int) for i in (a, b, c)):
            raise TypeError('значения сторон должны принадлежать натуральным числам')

        #Проверка что стороны a, b, c строго больше 0
        if not all(i > 0 for i in (a, b, c)):
            raise ValueError('значения a, b, c должны принадлежать натуральным числам')

        #Проверка что треугольник невырожденный
        if not all((a + b > c, a + c > b, b + c > a)):
            raise ValueError('треугольник должен быть невырожденным, т.е. каждая сторона должна строго меньше суммы двух других сторон')
        #наконец то проверки кончились
        self.a = a
        self.b = b
        self.c = c

    def calculate_ploshad(self):
        """
        Функция которая вычисляет площадь треугольника по трем сторонам

        :return: площадь

        Примеры:
        >>> triangle1 = Triangle(3, 4, 5)
        >>> triangle1.calculate_ploshad()
        """
        pass

    def is_right_triangle(self):
        """
        Функция которая проверяет является ли является ли этот треугольинк прямоугольным

        :return: является ли этот треугольинк прямоугольным

        Примеры:
        >>> triangle1 = Triangle(3, 4, 5)
        >>> triangle1.is_right_triangle()
        """
        pass

    def calculate_angles(self):
        """
        Функция которая вычисляет все углы в этом треугольнике
        :return: углы треугольника
        Примеры:
        >>> triangle1 = Triangle(3, 4, 5)
        >>> triangle1.calculate_angles()
        """
        pass


class Banka_piva():
#класс представляющий банку объемом 0,5 литров пива с определенной ценой за банку
    def __init__(self, name: str, price: int):
        """
        Инициализирует экземпляр класса Banka_piva
        :param name: Название пива
        :param price: Цена за банку пива

        Примеры:
        >>> pivo1 = Banka_piva('Bud', 70)
        """
        if not isinstance(name, str):
            raise TypeError('Название пива должно быть формата str')
        if not isinstance(price, int):
            raise TypeError('Цена пива должна быть целым положительным числом')
        if price<=0:
            raise ValueError('Цена пива должна быть >0')

        self.name = name
        self.price = price


    def price_10_banok_piva(self):
        """
        Функция, которая вычисляет цену 10 таких банок пива
        :return: цена
        Примеры:
        >>> pivo1 = Banka_piva('Bud', 70)
        >>> pivo1.price_10_banok_piva()
        """
        pass

    def calculate_amount(self, volume: int):
        """
        Функция, вычисляющая количество банок(объемом 0,5) в зависимости от требуемого объема,
        округляя количество в большую сторону

        :param volume: указанный объем
        :return: количество банок
        Пример:
        >>> pivo1 = Banka_piva('Bud', 70)
        >>> pivo1.calculate_amount(52)
        """
        if not isinstance(volume, int):
            raise TypeError('Объем должен быть целым положительным числом')
        if volume<=0:
            raise ValueError('Объем должен быть натуральным числом')


class Car:

    def __init__(self, brand: str, probeg: Union[int, float], color: str):
        """
        Инициализация экземпляра класса Car
        :param brand: бренд машины
        :param probeg: пробег машины
        :param color: цвет машины

        Пример:
        >>> car1 = Car('Matiz', 500, 'pink')
        """
        if not isinstance(brand, str):
            raise TypeError('Название машины должно быть формата str')
        if not isinstance(color, str):
            raise TypeError('Цвет машины должно быть формата str')
        if not isinstance(probeg, (float, int)):
            raise TypeError('Пробег должен быть формата float или int')
        if probeg < 0:
            raise ValueError('Пробег должен быть >=0')

        self.brand = brand
        self.probeg = probeg
        self.color = color

    def add_probeg(self, amount: Union[int, float]):
        """
        Функция, добавляющая пробег машине

        :param amount: количество на которое увеличить пробег
        :return:итоговый пробег машины
        пример:
        >>> car1 = Car('Matiz', 500, 'pink')
        >>> car1.add_probeg(650)
        """
        if not (isinstance(amount, (float, int)) and amount > 0):
            raise TypeError('количество должно быть формата float или int, а также больше 0')
        pass

    def print_car_info(self):
        """
        Функция которая возвращает информацию о машине(текущий пробег, название, цвет)
        :return: информацию о машине
        пример:
        >>> car1 = Car('Matiz', 500, 'pink')
        >>> car1.print_car_info()
        """
        pass



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()