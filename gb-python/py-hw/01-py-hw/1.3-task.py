"""
3.
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


n = int(input("Введите число n: "))
n_str1 = str(n)
n_str2 = n_str1 + n_str1
n_str3 = n_str1 + n_str1 + n_str1
n_comp = n + int(n_str2) + int(n_str3)
print(f"{n_str1} + {n_str2} + {n_str3} =", n_comp)
