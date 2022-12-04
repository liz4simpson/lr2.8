#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys


def get_train():
    name = input("Пункт назначения: ")
    number = input("Номер поезда: ")
    time_str = input("Время отправления: (hh:mm) ")
    time = datetime.datetime.strptime(time_str, '%H:%M').time()
    # Создать словарь.
    return {
        'name': name,
        'number': number,
        'time': time,
    }


def list_train(trains):
    # Заголовок таблицы.
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            time = train.get('time', '')
            print(
                '| {:>4} | {:<30} | {:<20} | {}{:>12} |'.format(
                    idx,
                    train.get('name', ''),
                    train.get('number', ''),
                    time,
                    ' ' * 5
                )
            )
        print(line)
    else:
        print('Список поездов пуст.')


def select_train(trains):
    p_n = input()
    count = 0
    # Проверка сведений из списка
    for train in trains:
        if train.get('name') == p_n:
            count += 1
            print('Пункт назначения:', train.get('name', ''))
            print('Номер поезда:', train.get('number', ''))
            print('Время отправления:', train.get('time', ''))

    if count == 0:
        print("Таких поездов нет!")


def main():
    trains = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            train = get_train()
            trains.append(train)
            if len(trains) > 1:
                # Сортировка
                trains.sort(key=lambda item: item.get('time', ''))
        elif command == 'list':
            list_train(trains)
        elif command.startswith('select'):
            select_train(trains)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select найти информацию о поезде по номеру")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
