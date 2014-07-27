"""
selection sort implementation
"""

def selection_sort(x):
    length = len(x)
    for i in range(0, length - 1):
        min = i
        for j in range(i + 1, length):
            if x[j] < x[min]:
                min = j
        if min != i:
            x[i], x[min] = x[min], x[i]
