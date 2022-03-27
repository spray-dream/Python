def ascending_order(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [1, 99, 5, 7, 9, 20, 11]
print(ascending_order(lst))
