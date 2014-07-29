"""
Project Euler 5:
Find the smallest multiple or numbers 1..20
"""


def gcd(x, y):
    # Implementing Euclide Algorithm: gcd(a, b) = gcd(b, a mod b)
    while(y != 0):
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)

print reduce(lcm, range(1, 21))
