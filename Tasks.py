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

def What_day(n):
    if n == 1:
        print('Пн')
    elif n == 2:
        print('Вт')
    elif n == 3:
        print('Ср')
    elif n == 4:
        print('Чт')
    elif n == 5:
        print('Пт')
    elif n == 6:
        print('Сб')
    else:
        print('Вс')
What_day(5)

# print('Введите N')
# N = int(input())
# for i in range(-N, N+1):
#     print(i)

# 6. Выяснить является ли число чётным
# n = 26
# print(n % 2 == 0)

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# import random

# Написать программу вычисления значения функции y = sin(x)/x
# from math import *
# def y(x):
#     return sin(x)/x
# print(y(28))

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