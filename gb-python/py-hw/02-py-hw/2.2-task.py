"""
2.2
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


user_data = input("Введите несколько элементов списка: ")
ls = []
x = 0
for i in user_data:
    ls.append(i)
print(f"Оригинальный список: {ls}")
for i in range(int(len(ls) / 2)):
    ls[x], ls[x + 1] = ls[x + 1], ls[x]
    x += 2
print(f"Модифицированный список:   {ls}")
