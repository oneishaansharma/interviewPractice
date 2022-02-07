# Given a string, compute recursively a new string where all the 'x' chars have been removed.


# noX("xaxb") → "ab"
# noX("abc") → "abc"
# noX("xx") → ""

def noX(string):
	if len(string) == 0:
		return ""
	elif (string[0]=='x'):
		return noX(string[1:])
	else:
		return string[0] + noX(string[1:])

res = noX('xxabcxxdefxx')

print(res)


