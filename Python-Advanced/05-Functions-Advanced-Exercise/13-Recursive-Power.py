# 13. Recursive Power

def recursive_power(number, power):
	if power == 1:
		return number
	return number * recursive_power(number, power - 1)


# Test Code:
print(recursive_power(2, 10))
print(recursive_power(10, 100))





















