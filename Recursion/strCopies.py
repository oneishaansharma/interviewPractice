# Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.


# strCopies("catcowcat", "cat", 2) → true
# strCopies("catcowcat", "cow", 2) → false
# strCopies("catcowcat", "cow", 1) → true

def strCopies(string, sub, num):
	if num <= strCopiesHelper(string, sub):
		return True
	return False

def strCopiesHelper(string, sub):
	if len(string) < len(sub):
		return 0
	else:
		if string[0:len(sub)] == sub:
			return 1 + strCopiesHelper(string[1:],sub)
		else:
			return strCopiesHelper(string[1:],sub)

print(strCopies("ababacatcowcat", "aba", 2))