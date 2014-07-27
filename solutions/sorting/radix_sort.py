"""
radix sort implementation

Wiki radix sort implementation
"""
from math import log

def radix_sort(x, base):

    def getDigit(num, base, digit_num):
        #return the selected digit of a number
        return (num // base ** digit_num) % base

    def makeBlanks(size):
        #create a list of empty lists to hold the split by digit
        return [[] for _ in xrange(size)]

    def split(num_list, base, digit_num):
        #split given list by numbers and sort them into list of lists
        #ex: [123, 143 , 124, 125, 12, 14, 19] will sort into:
        # [[12, 14, 19], [123, 143], [124], [125]] according to the LSD radix sort
        buckets = makeBlanks(base)
        for num in num_list:
            buckets[getDigit(num, base, digit_num)].append(num)
        return buckets

    def merge(num_list):
        #after splitting concantenate lists back in order for next step
        new_list = []
        for sublist in num_list:
            new_list.extend(sublist)
        return new_list

    def maxAbs(num_list):
        #get largest abs value element of a list (need to compute the number of needed steps)
        #ex: if maxAbs: 1234, then there'l be 4 steps
        return max(abs(num) for num in num_list)

    steps = int(round(log(maxAbs(x), base)) + 1)
    new_list = x[:]
    for digit_num in range(steps):
        new_list = merge(split(new_list, base, digit_num))
    return new_list


