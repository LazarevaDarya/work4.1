#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Num:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите дробное число: "))
        self.second = float(input("Введите еще одно дробное число: "))

    def display(self):
        print(f"Результат: ", power(self.first, self.second))


def power(first, second):
    if first == 0:
        raise ValueError
    else:
        return first ** second


if __name__ == "__main__":
    newNumber = Num(3.1,4.6)
    newNumber.display()
    newNumber.read()
    newNumber.display()