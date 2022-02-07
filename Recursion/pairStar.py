# Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".


# pairStar("hello") → "hel*lo"
# pairStar("xxyy") → "x*xy*y"
# pairStar("aaaa") → "a*a*a*a"


def pairStar(string,idx):
	if(len(string)<2): return string
	if idx==len(string)-1:
		return string[idx]
	else:
		if string[idx] == string[idx+1]:
			return string[idx] + "*" + pairStar(string,idx+1)
		else:
			return string[idx] + pairStar(string,idx+1)

print(pairStar("hello yellow successfully aaaa bbbb  ((",0))