# Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.


# countX("xxhixx") → 4
# countX("xhixhix") → 3
# countX("hi") → 0

def countx(string):
	if string == '':
		return 0
	else:
		if(string[-1]=='x'):
			return 1 + countx(string[0:-1])
		else:
			return countx(string[0:-1])

res = countx('xxhxxixx')

print(res)
