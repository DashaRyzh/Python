# 25. Написать программу преобразования десятичного числа в двоичное.
def decimal_to_binary(n):
    base = 2
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= base
    return result
print(decimal_to_binary(25))