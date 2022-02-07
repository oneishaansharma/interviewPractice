# Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.


# countHi("xxhixx") → 1
# countHi("xhixhix") → 2
# countHi("hi") → 1

def countHi(string):
	if len(string)<=2:
		if(string=='hi'):
			return 1
		else: 
			return 0

	else:
		if string[-2:] == 'hi':
			return 1 + countHi(string[0:-2])
		else:
			return countHi(string[:-1])


print(countHi('xhihihixhixhix'))
