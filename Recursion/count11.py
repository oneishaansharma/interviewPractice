# Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.


# count11("11abc11") → 2
# count11("abc11x11x11") → 3
# count11("111") → 1

def count11(string):
	if (len(string)<2):
		return 0
	else:
		if string[0:2] == "11":
			return 1 + count11(string[2:])
		else:
			return count11(string[1:])

string = "abc11x11x11x111"
print(count11(string))