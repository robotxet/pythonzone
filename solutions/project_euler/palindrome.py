"""
Project Euler 4:
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91x99.
Find the largest palindrome made from the product of two 3-digit numbers
"""
import math
import time


def is_palindrome(n):
    x = n
    rev = 0
    while x != 0:
        d = x % 10
        x = math.floor(x / 10)
        rev = (rev * 10) + d
    if rev == n:
        return True
    else:
        return False


def is_palindrome2(n):
    # This realisation is more than 3 times faster than previous
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def check_palindrome():
    result = 0
    start = time.time()
    min = 100
    max = 999
    for i in range(min, max + 1):
        for j in range(i + 1, max + 1):
            num = i * j
            if is_palindrome2(num):
                if num > result:
                    result = num
    elapsed = time.time() - start
    print "Total time %s" % elapsed
    return result


print check_palindrome()
