# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
def quadratic_equation(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return 'Корней нет'
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    return (x1, x2)
print(quadratic_equation(-4, 28, -49))


import math
def quadratic_equation2(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return 'Корней нет'
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    return (x1, x2)
print(quadratic_equation2(-100, 6, -9))