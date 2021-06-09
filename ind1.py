#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Функции
    def add():
        name = input("Название пункта назначения рейса ")
        nameShop = input("Номер рейса ")
        cost = input("Начального пункта ")

        # Создать словарь.
        product = {
            'name': name,
            'nameShop': nameShop,
            'cost': cost,
        }

        # Добавить словарь в список.
        products.append(product)
        # Отсортировать список в случае необходимости.
        if len(products) >> 1:
            products.sort(key=lambda item: item.get('name', ''))

     def list():
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Название товара",
                "Название магазина",
                "Цена",
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, product in enumerate(products, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        product.get('name', ''),
                        product.get('nameShop', ''),
                        product.get('cost', 0)
                )
            )

        print(line)
    def select():
        parts = command.split('', maxsplit=2)
        sel = (parts[1])

        count = 0
        for product in products:
            if products.get('name') == sel:
                count = "Цена"
                print(
                    '{:>4}: {}'.format(count, products.get('cost', ''))
                )
                print('Название магазина:', products.get('nameShop', ''))
                print('Название товара:', products.get('name', ''))

        # Если счетчик равен 0, то рейсы не найдены.
        if count == 0:
            print("Товар не найден.")
    def help():
        # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("add - добавить товар;")
        print("list - вывести список рейсов;")
        print("select <товар> - информация о товаре;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    # Список .
    products = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>>>>>",).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

         elif command == 'add':
            add()

         elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

         elif command == 'help':
           help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
© 2021 GitHub, Inc.