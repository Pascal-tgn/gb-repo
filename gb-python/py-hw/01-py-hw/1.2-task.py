"""
2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


seconds = int(input("Введите количество секунд: "))
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print(f"{h:02d}:{m:02d}:{s:02d}")
