# Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.


# strDist("catcowcat", "cat") → 9
# strDist("catcowcat", "cow") → 3
# strDist("cccatcowcatxx", "cat") → 9

def strDist(string, sub):
	if len(string) < len(sub):
		return 0
	else:
		if string[0:len(sub)]==sub and string[-len(sub):] == sub:
			return len(string)
		elif string[0:len(sub)]==sub:
			return strDist(string[0:len(string)-1],sub)
		elif string[-len(sub):] == sub:
			return strDist(string[1:],sub)
		else:
			return strDist(string[1:-1],sub)

print(strDist("cccatcowcatxx", "cat"))
