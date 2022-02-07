# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
list = ['q', 't' 'w', 'e', 't', 'q']
str = 'w' 
def check_enter(list, str):
    count = 0
    i = 0
    while i < len(list):
        if list[i] == str: count += 1
        if count == 2: return i+1
        i += 1
        if i == len(list): return -1
print(check_enter(list, str))