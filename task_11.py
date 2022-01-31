# 11. Для натурального N создать список из N членов последовательности:
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
def sequence(N):
    list = []
    i = 1
    list.append(i)
    n = 0
    while n < N - 1:
        new_i = i * -3
        list.append(new_i)
        i = new_i
        n += 1
    print(list)
    return list
sequence(7)