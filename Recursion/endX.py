# Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.


# endX("xxre") → "rexx"
# endX("xxhixx") → "hixxxx"
# endX("xhixhix") → "hihixxx"


def endX(string):
	if len(string) == 0:
		return ""
	else:
		if (string[0] == 'x'):
			return endX(string[1:]) + "x"
		else:
			return string[0] + endX(string[1:])

print(endX('xxre'))
print(endX('xhixhix'))
