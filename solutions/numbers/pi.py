"""
Find PI to the Nth Digit
Enter a number and program will generate PU up to that many decimal places.
Keep a limit to how far the program will go.
"""

import math

n = int(raw_input("How many spaces? "))

while n > 50:
    print "Number is out of limit"
    n = int(raw_input("How many spaces? "))
else:
    print "%.*f" % (n, math.pi)
