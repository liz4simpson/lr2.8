#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def cylinder():
    a = input("Введите число 1, если хотите получить площадь боковой поверхности цилиндра\n"
              "Введите число 2, если хотите получить полную площадь цилиндра: \n")
    r = int(input("Введите радиус: "))
    h = int(input("Введите высоту цилиндра: "))

    if a == '1':
        print("Площадь боковой поверхности цилиндра: ", 2 * math.pi * r * h)

    elif a == '2':
        print("Площадь боковой поверхности цилиндра: ", (2 * math.pi * r * h) + (circle(r) * 2))


def circle(r):
    return math. pi * (r ** 2)


if __name__ == '__main__':
    cylinder()

