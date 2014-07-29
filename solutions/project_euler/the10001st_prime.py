"""
Project Euler 7:
Find the 10001st prime number
"""


def is_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def nth_prime(n):
    nth = 1
    result = 1
    count = 1
    while count <= n:
        if is_prime(nth):
            result = nth
            count += 1
        nth += 1
    return result

print nth_prime(10001)
