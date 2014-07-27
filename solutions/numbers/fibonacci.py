def fib_recursive(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	return fib_recursive(x - 1) + fib_recursive(x - 2)

def fib_polynom(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	polynom = [0, 1]
	for i in range(2, x + 1):
		polynom.append(polynom[i - 1] + polynom[i - 2])
	return polynom[x]
