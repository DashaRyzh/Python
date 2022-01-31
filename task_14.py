# 14. Подсчитать сумму цифр в вещественном числе.
def sum(n):
    string_n = str(n)
    total = 0
    for i in string_n:
        if i == '.':
            total += 0
        else:
            total += int(i)
    print(total)
    return total
sum(1.2354)