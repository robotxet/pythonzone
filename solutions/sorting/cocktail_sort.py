"""
coctail sort implementaion
"""

def coctail_sort(x):
    swapped = True
    length = len(x) - 1
    begin = -1
    end = length
    while swapped:
        swapped = False
        begin += 1
        for i in range(begin, end):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, begin, -1):
            if x[i] < x[i - 1]:
                x[i], x[i - 1] = x[i - 1], x[i]
                swapped = True
