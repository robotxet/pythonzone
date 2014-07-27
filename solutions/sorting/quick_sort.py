"""
quick sort implementaion
"""

def quick_sort(x, begin, end):
    if begin < end:
        p = partition(x, begin, end)
        quick_sort(x, begin, p)
        quick_sort(x, p + 1, end)

def partition(x, begin, end):
    pivot = x[end - 1]
    storeIndex = begin - 1
    for j in range(begin, end - 1):
        if x[j] < pivot:
            storeIndex += 1
            x[storeIndex], x[j] = x[j], x[storeIndex]
    x[storeIndex + 1], x[end - 1] = x[end - 1], x[storeIndex + 1]
    return storeIndex + 1

def short_quick_sort(x):
    if len(x) <= 1:
        return x
    else:
        return short_quick_sort([i for i in x[1:] if i < x[0]]) + [x[0]] + short_quick_sort([i for i in x[1:] if i > x[0]])
