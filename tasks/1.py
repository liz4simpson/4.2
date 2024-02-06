#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.
"""


class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int):
            raise TypeError("Оба поля (first и second) должны быть целыми числами")

        if second == 0:
            raise ValueError("Знаменатель (second) не может быть равен нулю")

        self.first = first
        self.second = second

    def __floordiv__(self, other):
        """
        Перегрузка оператора для выделения целой части от деления.
        """
        if isinstance(other, Pair):
            if other.second != 0:
                return self.first // other.second
            else:
                raise ValueError("Невозможно вычислить целую часть при нулевом знаменателе")
        else:
            raise TypeError("Операнд должен быть объектом класса Pair")

    def __str__(self):
        """
        Перегрузка метода str для вывода дроби.
        """
        return f"({self.first}/{self.second})"

    def display(self):
        print(str(self))

    @classmethod
    def read(cls):
        a = int(input("Введите числитель: "))
        b = int(input("Введите знаменатель: "))

        return cls(a, b)


if __name__ == "__main__":
    pair = Pair.read()
    pair.display()
    other_pair = Pair.read()
    print("Целая часть:", pair // other_pair)