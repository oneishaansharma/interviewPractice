# Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.


# strCount("catcowcat", "cat") → 2
# strCount("catcowcat", "cow") → 1
# strCount("catcowcat", "dog") → 0

def strCount(string,sub):
	if len(string) < len(sub):
		return 0
	else:
		if(string[0:len(sub)] == sub):
			return 1 + strCount(string[len(sub):],sub)
		else:
			return strCount(string[1:],sub)

res = strCount("catcowcat","cat")
print(res)