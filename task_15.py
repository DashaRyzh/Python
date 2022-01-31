# Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
def set_of_products(N):
    list = []
    i = 1
    product = 1
    while i <= N:
        product *= i
        i += 1
        list.append(product)
    print(list)
    return list
set_of_products(10)
