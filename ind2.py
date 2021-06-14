#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import os.path

if __name__ == '__main__':
    products = []
    list_file = 'c:\\products.txt'
    def add():
        global products
        name = input("Название товара ")
        nameshop = input("Название магазина ")
        cost = input("Цена ")

        product = {
            'name': name,
            'nameshop': nameshop,
            'cost': cost,
        }

        products.append(product)
        if len(products) > 1:
            products.sort(key=lambda item: item.get('name', ''))


    def list():
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
                "Цена"
            )
        )
        print(line)

        for idx, product in enumerate(products, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('nameshop', ''),
                    product.get('cost', 0)
                )
            )
        print(line)


    def select():
        sel = input('Название товара ')
        count = 0
        for idx, product in enumerate(products, 1):
            if product.get('name') == sel:
                count = "Цена"
                print(
                    '{:>4}: {}'.format(count, product.get('cost', ''))
                )
                print('Название магазина:', product.get('nameshop', ''))
                print('Название товара:', product.get('name', ''))
        if count == 0:
            print("Товар не найден.")


    def load():
        global products
        if os.path.exists(list_file):
            with open(list_file, "r") as f:
                products = json.load(f)


    def save():
        global products
        with open(list_file, 'w') as f:
            json.dump(products, f)


    def help():
        print("Список команд:\n")
        print("add - добавить товар;")
        print("list - вывести список товаров;")
        print("select <товар> - информация о товаре;")
        print("help - отобразить справку;")
        print("save  - сохранить данные в файл;")
        print("load  - загрузить данные из файла;")
        print("exit - завершить работу с программой.")


    while True:
        command = input(">>>>>>", ).lower()

        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'save':
            save()

        elif command == 'load':
            load()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
            help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
