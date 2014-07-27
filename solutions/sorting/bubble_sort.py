"""
bubble_sort implementaion

average complexity: O(n*n)
"""

def bubble_sort(x):
    length = len(x)
    for i in range(1, length):
        sorted = False
        for j in range(1, length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                sorted = True
        if not sorted:
            break
