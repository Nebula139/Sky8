#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

if __name__ == '__main__':
    # Функции
    def add():
        name = input("Название товара ")
        nameShop = input("Название магазина ")
        cost = input("Цена ")

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

        if count == 0:
            print("Товар не найден.")


    def load():
        # Разбить команду на части для выделения имени файла.
        parts = command.split(' ', maxsplit=1)
        # Прочитать данные из файла JSON.
        with open(parts[1], 'r') as f:
            station = json.load(f)


    def save():
        # Разбить команду на части для выделения имени файла.
        parts = command.split(' ', maxsplit=1)
        # Сохранить данные в файл JSON.
        with open(parts[1], 'w') as f:
            json.dump(products, f)

    def help():
        # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("add - добавить товар;")
        print("list - вывести список товаров;")
        print("select <товар> - информация о товаре;")
        print("help - отобразить справку;")
        print("save 'имя файла' - сохранить данные в файл;")
        print("load 'имя файла' - загрузить данные из файла;")
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
            print("Неизвестная команда {command}", file=sys.stderr