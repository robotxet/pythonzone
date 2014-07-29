"""
Project Euler 6:
Find the difference between the sum of the squares of the first one
hundred natural numbers and the square sum
"""


def sum_squares(x):
    sum = 0
    for x in range(1, 101):
        sum += x ** 2
    return sum


def square_sum(x):
    sum = 0
    for x in range(1, 101):
        sum += x
    return sum ** 2

print square_sum(100) - sum_squares(100)
