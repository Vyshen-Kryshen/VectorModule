"""

"""
from math import sqrt


class Vector:
    """
    Векторный тип данных.
    """
    __numbers: tuple[int | float, ...] = ()
    __length: int | float = 0.0

    def __init__(self, *numbers: int | float | tuple[int | float, ...]) -> None:
        """
        Инициализация и проверка переданных аргументов в параметры
        :param nums:
        """
        for index, number in enumerate(numbers):
            if isinstance(number, int) or isinstance(number, float):
                self.__numbers = numbers
            elif isinstance(number, tuple):
                self.__numbers = number
            elif isinstance(number, type(self)):
                self.__numbers = number.__numbers
                self.__length = number.__length
            else:
                raise ValueError(f"Wrong type of argument - {number} - at index {index}!. Type of this object is: "
                                 f"{type(number)}")

    def __getitem__(self, item: int) -> int | float:
        """
        Магический метод для индексирования объекта этого типа.
        :param item:
        :return:
        """
        return self.__numbers[item]

    def __repr__(self) -> str:
        """
        Строковое репродуктивное представление объектов данного класса.
        :return:
        """
        return f"{self.__numbers}"

    def __add__(self, other) -> tuple[int | float, ...]:
        """
        Магический метод для реализации левого сложения вектора с вектором или вектора со скаляром.
        :param other:
        :return:
        """
        if isinstance(other, type(self)):
            result: list[int | float] = []
            if len(self.__numbers) < len(other.__numbers):
                for index, number in enumerate(self.__numbers):
                    result.append(number + other.__numbers[index])
                else:
                    return tuple(result)
            else:
                for index, number in enumerate(other.__numbers):
                    result.append(number + self.__numbers[index])
                else:
                    return tuple(result)
        elif isinstance(other, int) or isinstance(other, float):
            result: list[int | float] = []
            for number in self.__numbers:
                result.append(number + other)
            else:
                return tuple(result)
        else:
            raise ValueError(f"Wrong type on object-argument - {other}, so his type the - {type(other)}")

    def __radd__(self, other) -> tuple[int | float, ...]:
        """
        Магический метод для реализации правого сложения вектора с вектором или скаляра с вектором.
        :return:
        """
        if isinstance(other, int) or isinstance(other, float):
            result: list[int | float] = []
            for number in self.__numbers:
                result.append(number + other)
            else:
                return tuple(result)
        else:
            raise ValueError(f"Wrong type on object-argument - {other}, so his type the - {type(other)}")

    def __mul__(self, other) -> tuple[int | float, ...]:
        """
        Магический метод для реализации левого умножения вектора с вектором или вектора со скаляром.
        :param other:
        :return:
        """
        if isinstance(other, int) or isinstance(other, float):
            result: list[int | float] = []
            for number in self.__numbers:
                result.append(number * other)
            else:
                return tuple(result)
        elif isinstance(other, type(self)):
            result: list[int | float] = []
            if len(self.__numbers) < len(other.__numbers):
                for index, number in enumerate(self.__numbers):
                    result.append(number * other.__numbers[index])
                else:
                    return tuple(result)
            else:
                for index, number in enumerate(other.__numbers):
                    result.append(number * self.__numbers[index])
                else:
                    return tuple(result)
        else:
            raise ValueError(f"Wrong type on object-argument - {other}, so his type the - {type(other)}")

    def __rmul__(self, other) -> tuple[int | float, ...]:
        """
        Магический метод для реализации правого умножения вектора с вектором или скаляра с вектором.
        :param other:
        :return:
        """
        if isinstance(other, int) or isinstance(other, float):
            result: list[int | float] = []
            for number in self.__numbers:
                result.append(number * other)
            else:
                return tuple(result)
        else:
            raise ValueError(f"Wrong type on object-argument - {other}, so his type the - {type(other)}")

    def get_numbers(self) -> tuple[int | float, ...]:
        """
        Метод для возврата всех чисел экземпляра этого шаблона-вектора.
        :return:
        """
        return self.__numbers

    def calculate_length(self) -> int | float:
        """
        Метод для расчёта длины экземпляра этого шаблона-вектора.
        :return:
        """
        result: int | float = 0
        for number in self.__numbers:
            result += number ** 2
        else:
            self.__length = result
            return sqrt(result)

    def get_length(self) -> int | float:
        """
        Метод для возврата длины экземпляра этого шаблона-вектора.
        :return:
        """
        return self.__length

    def invert_lens(self) -> int | float:
        """
        Метод для возврата инверсии длины объекта.
        :return:
        """
        result: int | float = 1 / self.calculate_length()
        self.__length = result
        return result

    def normalize(self) -> tuple[int | float, ...]:
        """
        Этот метод реализует нормализацию объекта вектора.
        :return:
        """
        result: list[int | float] = []
        for number in self.__numbers:
            result.append(number * self.invert_lens())
        else:
            self.__numbers = tuple(result)
            return tuple(result)


if __name__ == '__main__':
    v1: Vector = Vector(1, 2, 3)
    v2: Vector = Vector(2, 3)
    print(Vector(Vector(v1 * 8).get_numbers()).normalize())
    speed: Vector = Vector(10, 5)
    print(sqrt(3.1415) * speed)
    while True:
        pass
