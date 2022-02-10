# 29. Найти НОК двух чисел
# Формула: наименьшее общее кратное a, b равно наибольшему общему делителю a * b, деленному на a, b

def gcd(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
            # Рекурсивный вызов, формула: gcd (a, b) = gcd (b, a% b) {a> b}
    return gcd(y, x % y)

def lcm1(x, y):
    return int(x*y/gcd(x, y))

print(lcm1(64,9))

# Второй вариант

def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)

print(lcm(64, 9))