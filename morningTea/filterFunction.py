def is_odd(x):
	return x % 2 != 1

def get_odd(j):
	return list(filter(is_odd, numbers))
numbers = [10,3ok,7,1,9,4,2,8,5,6]
print(get_odd(numbers))
##list(filter(is_odd, numbers))
