#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class String:
    """
    Класс String по примеру реализации класса из TurboPascal
    """

    MAX_SIZE = 255  # Максимальное количество символов в строке

    def __init__(self, string):
        """
        Конструктор класса, обязательный параметр - исходная строка
        """
        if len(string) > self.MAX_SIZE:
            raise ValueError("Строка слишком длинная")

        # Текущее количество символов в строке
        self.count = len(string)
        # Массив символов, первым элементом является длина
        self.data = [self.count] * (self.MAX_SIZE + 1)

        # Записываем все символы из строки в массив символов data
        for i, char in enumerate(string):
            self.data[i + 1] = char

    def size(self):
        """
        Длина строки
        """
        return self.count

    def __len__(self):
        """
        Перегруженный оператор для функции len, возвращает длину строки
        """
        return self.count

    def __str__(self):
        """
        Преобразование экземпляра класса в строку
        """
        string = ""

        for i in range(1, self.count + 1):
            string += self.data[i]

        return string

    def find(self, substring):
        """
        Поиск подстроки в строке, возвращает индекс, если подстрока не входит в строку - возвращает -1
        """
        sub_length = len(substring)

        for i in range(1, self.count - sub_length + 2):
            found = True

            for j in range(sub_length):
                if self.data[i + j] != substring[j]:
                    found = False
                    break

            if found:
                return i

        return -1

    def remove(self, substring):
        """
        Удаление подстроки из строки
        """
        sub_length = len(substring)
        index = self.find(substring)

        if index != -1:
            for i in range(index + sub_length, self.count + 1):
                self.data[i - sub_length] = self.data[i]
            self.count -= sub_length
            self.data[0] = self.count

    def __sub__(self, other):
        """
        Перегруженный оператор вычитания '-', удаляет подстроку из строки
        """
        self.remove(other)
        return self

    def insert(self, substring, index):
        """
        Вставка подстроки в строку в определенный индекс
        """
        sub_length = len(substring)
        if self.count + sub_length > self.MAX_SIZE:
            raise ValueError(f"Строка не может быть больше чем {self.MAX_SIZE}")

        for i in range(self.count, index - 1, -1):
            self.data[i + sub_length] = self.data[i]

        for i, char in enumerate(substring):
            self.data[index + i] = char

        self.count += sub_length
        self.data[0] = self.count

    def concatenate(self, other):
        """
        Конкатенация переданной строки в конец текущей строки
        """
        other_len = len(other)
        if self.count + other_len > self.MAX_SIZE:
            raise ValueError(f"Строка не может быть больше чем {self.MAX_SIZE}")

        for i in range(0, other_len):
            self.data[self.count + i + 1] = other[i]

        self.count += other_len
        self.data[0] = self.count

    def __add__(self, other):
        """
        Перегрузка оператора сложения, конкатенируют подстроку в конец текущей строки
        """
        self.concatenate(other)
        return self

    def __getitem__(self, item):
        """
        Перегрузка оператора [] - получение символа из строки по индексу
        """
        return self.data[item]


if __name__ == "__main__":
    s = String("Иванов")
    print(s)
    print(s.size())

    s += " Иван"
    print(s)
    print(s.size())
    print(s[12])

    s.remove("Иванов ")
    print(s)
    print(s.size())

    print(s.find("ва"))
    s.insert("44", 3)
    print(s)

    s.remove("44")
    print(s)

    s.concatenate(" Иванов")
    print(s)