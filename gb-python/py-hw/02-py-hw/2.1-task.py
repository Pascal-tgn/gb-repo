"""
2.1
 Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента.
 Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у пользователя,
 а указать явно, в программе.
 """


ls = [2, 1.2, 'abc', None, {}, (), [], {()}]
for i in ls:
    print(f"'{i}' - {type(i)}".replace('<class', 'type').replace('>', ''))
