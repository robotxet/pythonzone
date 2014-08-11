"""
onsider the following algorithm to generate a sequence of numbers.
Start with an integer n. If n is even, divide by 2. If n is odd,
multiply by 3 and add 1. Repeat this process with the new value of n,
terminating when n = 1.
"""


def three_plus_one(n):
    result = []
    result.append(n)

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        result.append(n)
    return result

print three_plus_one(22)
