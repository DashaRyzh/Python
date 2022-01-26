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

# 15. Дано число. Проверить кратно ли оно 7 и 23
# def Multiple1(n):
#     print(n % 7 == 0 and n % 23 == 0)
# Multiple1(161)

# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным
# def Is_weekend():
#     print('Введите число, обозначающее день недели:')
#     week_day = int(input())
#     if week_day > 0 and week_day < 6:
#         print('Будний день')
#     elif week_day >= 6 and week_day < 8:
#         print('Выходной день')
#     else:
#         print('Введите число от 1 до 7')
# Is_weekend()

# 17. По двум заданным числам проверять является ли одно квадратом другого
# def Is_square(a, b):
#     if a == b * b:
#         print("Число", a, "является квадратом числа", b)
#     elif b == a * a:
#         print("Число", b, "является квадратом числа", a)
#     else:
#         print(False)
# Is_square(16, 4)

# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y ⋀ Z
# def Logic(X, Y, Z):
#     return not(X or Y) == (not X and not Y and not Z)
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0,2):
#             print (Logic(x, y, z))
# Logic(1, 0, 0)

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

# 20. Задать номер четверти, показать диапазоны для возможных координат
# def Range(n):
#     import math
#     x = None
#     y = None
#     if n == 1:
#         print('x ∈', (0, math.inf), 'y ∈', (0, math.inf))
#     if n == 2:
#         print('x ∈', (-math.inf, 0), 'y ∈', (0, math.inf))
#     if n == 3:
#         print('x ∈', (-math.inf, 0), 'y ∈', (-math.inf, 0))
#     if n == 4:
#         print('x ∈', (0, math.inf), 'y ∈', (-math.inf, 0))
# Range(4)

# 21. Программа проверяет пятизначное число на палиндромом.
# def Palindrome(n):
#     if n % 10 == n // 10000 and (n // 10) % 10 == (n // 1000) % 10:
#         return print(True)
#     else:
#         return print(False)
# Palindrome(12321)

# 22. Найти расстояние между точками в пространстве 2D/3D
# x1 = 5
# x2 = 8
# y1 = 10
# y2 = 15
# d = (x2 - x1) ** 2 + (y2 - y1) ** 2
# D = d ** 0.5
# print(D)

# def Distance():
#     x1 = 5
#     x2 = 9
#     y1 = 3
#     y2 = 6
#     z1 = 7
#     z2 = 4
#     d = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
#     D = d**0.5
#     print(D)
#     return D
# Distance()

# 23. Показать таблицу квадратов чисел от 1 до N
# def Square(n):
#     i = 1
#     while i <= n:
#         print(i * i)
#         i += 1
# Square(5)

# 24. Найти кубы чисел от 1 до N
# def Cube(n):
#     i = 1
#     while i <= n:
#         print(i ** 3)
#         i += 1
# Cube(5)

# 25. Найти сумму чисел от 1 до А
# def Sum(A):
#     i = 1
#     res = 0
#     while i <= A:
#         res = res + i
#         i = i + 1
#     return res
# print(Sum(5))

# 26. Возведите число А в натуральную степень B используя цикл
# def Degree(a, b):
#     res = 1
#     for i in range(1, b + 1):
#         res *= a
#     return res
# print(Degree(2, 3))

# 27. Определить количество цифр в числе
# def Count(n):
#     count = 0
#     while n > 0:
#         n = n // 10
#         count += 1
#     return count
# print(Count(1234789))

# 28. Подсчитать сумму цифр в числе
# def Sum(n):
#     sum = n % 10
#     while n > 0:
#         n = n // 10
#         a = n % 10
#         sum = sum + a
#         n = n - a
#     return sum
# print(Sum(1231))

# 29. Написать программу вычисления произведения чисел от 1 до N
# def Product_of_num(N):
#     product = 1
#     i = 1
#     while i <= N:
#         product = product * i
#         i += 1
#     return product
# print(Product_of_num(5))

# 30. Показать кубы чисел, заканчивающихся на четную цифру
# def Even_cubes(n):
#     i = 1
#     while i <= n:
#         if (i ** 3) % 2 == 0:
#             print(i ** 3)
#         i += 1
#     return i ** 3
# Even_cubes(12)

# 31. Задать массив из 8 элементов и вывести их на экран
# import random
# def Array(list):
#     list = []
#     for i in range(0, 8):
#         i = random.randint(-10, 10)
#         list.append(i)
#     return print(list)
# Array(list)

# 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
# def Array(list):
#     import random
#     list = []
#     for i in range(0, 8):
#         i = random.randint(0, 1)
#         list.append(i)
#     return list
# print(Array(list))

# 33. Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива
# import random
# def Sum_array(list):
#     list = []
#     sum = 0
#     for i in range(0, 12):
#         i = random.randint(0, 9)
#         list.append(i)
#     print(list)
#     for i in list:
#         if i > 0:
#             sum = sum + i
#             i += 1
#     print(sum)
# Sum_array(list)

# 34. Написать программу замены элементов массива на противоположные
# mass1 = [1, 3, -7, 31, 28, -67]
# for i in mass1:
#     print(i * -1)

# 35. Определить, присутствует ли в заданном массиве, некоторое число
# import random
# def Number(min_value, max_value, n):
#     list = []
#     for num in range(min_value, max_value):
#         num = random.randint(1, 9)
#         list.append(num)
#     print(list)
#     if list[num] == n:
#         print(True)
#     else:
#         print(False)
# Number(1, 11, 8)

# 36. Задать массив, заполнить случайными положительными трёхзначными числами.
# Показать количество нечетных\четных чисел
# import random
# def Count_of_num(min_value, max_value):
#     array = []
#     count_of_even = 0
#     count_of_not_even = 0
#     for num in range(min_value, max_value):
#         num = random.randint(100, 999)
#         array.append(num)
#     for num in array:
#         if num % 2 == 0:
#             count_of_even += 1
#         else:
#             count_of_not_even += 1
#     print(array)
#     print(f'Чётных элементов: {count_of_even}')
#     print(f'Нечётных элементов: {count_of_not_even}')
# Count_of_num(1, 11)
