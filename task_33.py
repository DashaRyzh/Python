# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from operator import length_hint
import random
def koef(k):
    li = []
    for i in range(k+1):
          li.append(random.randint(0,100))
    return(li)
li = koef(3)
length = len(li)
def el(li, k, l):
    res_list = ''
    for m in range(0, l):
        if k==1: res_list +=(f'{li[m]}*x +')
        elif k==0: res_list +=(f'{li[m]} = 0')
        else:
            res_list +=(f'{li[m]}*x^{k} +')
        k -=1
    return(res_list)

#print (el(li, 4))

result = el(li, 3, length)
print(result)
with open ("33.txt", 'w') as file:
    file.write(result)
