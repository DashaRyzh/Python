# 16. Задать список из n чисел последовательности (1+1/n)*n и вывести на экран их сумму
def sequence(n):
    lst = []
    k = 1
    while k <= n:
        lst.append((1 + 1/k)*k)
        k += 1
    return lst
print(sequence(4))