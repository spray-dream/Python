# -*- coding = utf-8 -*-
# @Time : 2021/12/5 23:57
# @Author : spray_dream
# @File : 020-归并排序.py
# @Software: PyCharm

def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append((right[r]))
            r += 1
    result += left[l:]
    result += right[r:]
    return result

alist = [4, 5, 6, 1, 2, 3]
print(merge_sort(alist))

"""
merge_sort(alist = [54, 26, 93, 17, 77, 31, 44, 55, 20])

    一-1 left = merge_sort(alist = [54, 26, 93, 17  ||  77, 31, 44, 55, 20])                              n = 9  mid = 4

        二-1 left = merge_sort(alist = [54, 26  ||  93, 17])   分好了之后程序停在12行                        n = 4, mid = 2

            三-1 left = merge_sort(alist = [54  ||  26])                                                  n = 2, mid = 1

                三-1-- left = alist = 54                                                              n = 1  return三结束

            三-2 right = merge_sort(alist = [54  ||  26])               在13行及以下

                三-2-- right = alist = 26                                                                

            三-3 执行while, result = [26, 54]                                    二-1 left = [26, 54]

        二-2 right = merge_sort(alist = [54, 26  ||  93, 17])           在13行及以下

            二-2-1 left = merge_sort(alist = [93  ||  17])

                二-2-1-- left = alist = 93

            二-2-2 right = merge_sort(alist = [93  ||  17])

                二-2-2-- right = alist = 17 

            二-2-3 执行while, result = [17, 93]                                  二-2 right = [17, 93]
            
        二-3 执行while, result = [17, 26, 54, 93]                      一-1的left = [17, 26, 54, 93]

    一-2 right = merge_sort(alist = [54, 26, 93, 17  ||  77, 31, 44, 55, 20])
    
        一-2-1 left = merge_sort(alist = [77, 31  ||  44, 55, 20])
            
            一-2-1-1 left = merge_sort(alist = [77  ||  31])

                一-2-1-1-- left = alist = 77

            一-2-1-2 right = merge_sort(alist = [77  ||  31])

                一-2-1-2-- right = alist = 31

            一-2-1-3 执行while, result = [31, 77]                                 一-2-1 left = [31, 77]

        一-2-2 right = merge_sort(alist = [77, 31  ||  44, 55, 20])

            一-2-2-1 left = merge_sort(alist = [44  ||  55, 20)

                一-2-2-1-- left = alist = 44

            一-2-2-2 right = merge_sort(alist = [44  ||  55, 20])

                一-2-2-2-1 left = merge_sort(alist = [55  ||  20])

                    一-2-2-2-1-- left = alist = 55

                一-2-2-2-2 right = merge_sort(alist = [55  ||  20])

                    一-2-2-2-2-- right = alist = 20

                一-2-2-2-3 执行while, result = alist = [20, 50]                         一-2-2-2 right = [20, 50]

            一-2-2-3 执行while, result = alist = [20, 44, 54]                     一-2-2 right = [20, 44, 54]

        一-2-3 执行while, result = alist = [20, 31, 44, 54, 77]              一-2 right = [20, 31, 44, 54, 77]

    一-3 执行while, result = alist = [17, 20, 26, 31, 44, 54, 54, 77, 93]
"""
