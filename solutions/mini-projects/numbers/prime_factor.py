"""
Prime factorization:
Have the user enter a number and find all prime factors (if there any)
and display them.
"""


def is_prime(n):
    if n % 2 == 0:
        return False

    for x in range(3, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

number = raw_input("Enter number: ")
isNumber = False

while(not isNumber):
    try:
        number = int(number)
    except ValueError:
        print("Number must be int. Please try again.")
        isNumber = False
        number = raw_input("Enter number: ")
    else:
        isNumber = True

prime_factors = [1]

if number % 2 == 0:
    prime_factors.append(2)

for n in range(3, int(number / 2) + 1):
    if number % n == 0:
        if is_prime(n):
            prime_factors.append(n)

print prime_factors
