"""
Next prime number:
Have the program find prime numbers until chooses to stop asking for
next
"""


def is_prime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

ask = True
number = 1
while(ask):
    decision = raw_input("Next prime? (y/n)")
    if decision.startswith("n"):
        ask = False
    elif decision.startswith("y"):
        if number == 1:
            print number
        elif number == 2:
            print number
        else:
            while(not is_prime(number)):
                number += 1
            print number
        number += 1
