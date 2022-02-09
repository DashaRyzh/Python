# 27. Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
def max_min():
    li = []
    print('Введите числа:')
    a = str(input())
    b = a.split()
    li = [int(i) for i in b]
    max_n = max(li)
    min_n = min(li)
    return (max_n, min_n)
print(max_min())