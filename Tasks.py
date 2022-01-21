# import random
# a = random.randint(2, 23)
# print(a)

# 0. Вывести квадрат числа
# def Square(n):
#     return print(n * n)
# Square(3)

# 1. По двум заданным числам проверять является ли первое квадратом второго
# def Is_square(a, b):
#     if a == b * b:
#         return print(True)
#     else:
#         return print(False)
# Is_square(4, 2)

# 2. Даны два числа. Показать большее и меньшее число
# def Max_num(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# Max_num(20, 8)

# 3. По заданному номеру дня недели вывести его название
# def What_day(n):
#     if n == 1:
#         print('Пн')
#     elif n == 2:
#         print('Вт')
#     elif n == 3:
#         print('Ср')
#     elif n == 4:
#         print('Чт')
#     elif n == 5:
#         print('Пт')
#     elif n == 6:
#         print('Сб')
#     else:
#         print('Вс')
# What_day(2)

# 4. Найти максимальное из трех чисел
# def Max(a, b, c):
#     max = a
#     if b > max:
#         max = b
#     if c > max:
#         max = c
#     print(max)
# Max(1, 30, 7)

# 5. Написать программу вычисления значения функции y = sin(x)/x
# from math import *
# def y(x):
#     return sin(x)/x
# print(y(28))

# 6. Выяснить является ли число чётным
# def Is_even(n):
#     print(n % 2 == 0)
# Is_even(27)

# 7. Показать числа от -N до N
# print('Введите N')
# N = int(input())
# for i in range(-N, N+1):
#     print(i)

# 8. Показать четные числа от 1 до N
# def Even_num(N):
#     if N > 0:
#         for i in range(1, N + 1):
#             if i % 2 == 0:
#                 print(i)
#     else:
#         for i in range(N, 2):
#             if i % 2 == 0:
#                 print(i)
# Even_num(10)

# 9. Показать последнюю цифру трёхзначного числа
# def Last_digit(n):
#     print(n % 10)
# Last_digit(249)

# 10. Показать вторую цифру трёхзначного числа
# def Second_digit(n):
#     print((n // 10) % 10)
# Second_digit(200)

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# def Max_digit(n):
#     max = n % 10
#     if n // 10 > max:
#         max = n // 10
#     print('Наибольшая цифра числа', n, ':', max)
# Max_digit(87)

# 12. Удалить вторую цифру трёхзначного числа
# def Delete_second_digit(n):
#     last = str(n % 10)
#     first = str(n // 100)
#     print(first + last)
# Delete_second_digit(437)

# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
# def Multiple(a, b):
#     print(a % b == 0)
# Multiple(12, 4)

# 14. Найти третью цифру числа или сообщить, что её нет
# def Third_digit(n):
#     if n // 100 == 0:
#         print('В данном числе нет третьей цифры')
#     else:
#         print((n // 100) % 10)
# Third_digit(567489)

# 22. Найти расстояние между точками в пространстве 2D/3D
# x1 = 5
# x2 = 8
# y1 = 10
# y2 = 15
# d = (x2 - x1) ** 2 + (y2 - y1) ** 2
# D = d ** 0.5
# print(D)

# 34. Написать программу замену элементов массива на противоположные
# mass1 = [1, 3, -7, 31, 28, -67]
# for i in mass1:
#     print(i * -1)

# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y


# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
# x = 5
# y = -3
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# else:
#     print('4 четверть')