"""
Factorial Finder
"""


def fact_recursive(x):
    if x < 0 or x >= 1000:
        return "Error: invalid input (recursive doesn't support \
            values equal or more than 1000"
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * fact_recursive(x - 1)


def fact_polynom(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    fact = [1, 1]
    for i in range(2, x + 1):
        fact.append(i * fact[i - 1])
    return fact[x]

# no check if number is int
number = raw_input("Enter factorial number: ")
print "recursive: %s" % fact_recursive(int(number))
print "polynom: %s" % fact_polynom(int(number))
