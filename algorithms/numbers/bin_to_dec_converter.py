"""
Binary To Decimal Converter
"""

conv_type = raw_input("Enter bin for Binary To Decimal conversion or dec for Decimal To Binary convertion: ")
number = raw_input("Enter number: ")

if conv_type == "bin":
    print int(number, 2)
elif conv_type == "dec":
    print bin(int(number))
else:
    print "Unknown conversion type"
