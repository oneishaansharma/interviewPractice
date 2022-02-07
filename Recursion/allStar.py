# Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".


# allStar("hello") → "h*e*l*l*o"
# allStar("abc") → "a*b*c"
# allStar("ab") → "a*b"

def allStar(string):
	if(len(string)==1):
		return string
	else:
		return string[0] + "*" + allStar(string[1:])

print(allStar("hello world"))