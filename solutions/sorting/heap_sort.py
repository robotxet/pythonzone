"""
Heap sort implementation
according to Wiki:heapsort
"""
import math

def heapsort(x):
    def heapify(x, len):
        start = (len - 2) / 2

        while start >= 0:
            sift(x, start, len - 1)
            start -= 1

    def sift(x, begin, end):
        root = begin

        while root * 2 + 1 <= end:
            child = root * 2 + 1
            swap = root

            if x[swap] < x[child]:
                swap = child
            if child + 1 <= end and x[swap] < x[child + 1]:
                swap = child + 1
            if swap != root:
                x[root], x[swap] = x[swap], x[root]
                root = swap
            else:
                return

    length = len(x)

    heapify(x, length)

    end = length - 1
    while end > 0:
        x[end], x[0] = x[0], x[end]
        end -= 1
        sift(x, 0, end)
