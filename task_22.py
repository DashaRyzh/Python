# 22. Найти сумму чисел списка стоящих на нечетной позиции.
import random
new_list = [random.randint(1, 10) for i in range(1, 11)]
my_list = new_list

def odd_position(your_list):
    i = 0
    sum = 0
    while i <= len(my_list):
        if i % 2 != 0:
            sum += my_list[i]
        i += 1
    print(my_list)
    return sum


print(odd_position(my_list))