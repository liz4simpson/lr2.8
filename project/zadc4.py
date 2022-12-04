#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    # Вводиться строка с буквами или числами
    a = input("Введите строку: ")
    return a


def test_input(stroka):
    # Проверяем, возможно ли значение strok привести к числу
    if type(stroka) == int:
        return True
    elif stroka.isnumeric():
        return True
    else:
        return False


def str_to_int(strok):
    # Идёт преобразование strok к целочисленному формату
    a = int(strok)
    return a


def print_int(stroka):
    # Выводим значение на экран
    print(stroka)


if __name__ == '__main__':
    stroka = get_input()
    proverka = test_input(stroka)
    if proverka is True:
        print_int(str_to_int(stroka))
    else:
        print("Введённая строка не является числом")