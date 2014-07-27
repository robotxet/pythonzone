"""
Project Euler 3:
The prime factors of 13195 are 5, 7, 13 and 29

What is the largest prime factor of the number 600851475143?
"""

def is_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def largest_prime(x):
    prime_factors = 1
    if x % 2 == 0:
        prime_factors = 2
        x /= 2
    i = 3
    while i <= int(x ** 0.5) + 1:
        if x % i == 0 and is_prime(i):
            prime_factors = i
        i += 1
    return prime_factors

print largest_prime(600851475143)


