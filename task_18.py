# 18. Реализовать алгоритм перемешивания списка. 
import random
my_list = [random.randint(1, 100) for i in range(1, 15)]
print(my_list)
def mix(my_list):
    iteration = len(my_list) / 2
    temp_var = 0
    while iteration > 0:

        for i in range(0, len(my_list)):
            for j in range(0, len(my_list)):
                temp_var = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp_var
            iteration -= 1
        return my_list
print(mix(my_list))
