# We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.


# countPairs("axa") → 1
# countPairs("axax") → 2
# countPairs("axbx") → 1

def countPairs(string):
	if (len(string)<3):
		return 0
	else:
		if (string[0]==string[2]):
			return 1 + countPairs(string[1:])
		else:
			return countPairs(string[1:])
print(countPairs('axaxaxaxxx'))