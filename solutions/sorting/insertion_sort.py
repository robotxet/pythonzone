"""
insertion sort implementaion
"""


def insertion_sort(x):
    if len(x) < 2:
        return
    for i in range(1, len(x)):
        for j in range(i, 0, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
