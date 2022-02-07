# Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".


# parenBit("xyz(abc)123") → "(abc)"
# parenBit("x(hello)") → "(hello)"
# parenBit("(xy)1") → "(xy)"


def parenBit(string):
	return parenBitHelper(string, 0, len(string)-1)

def parenBitHelper(string, start_idx, end_idx):
	if string[start_idx] == "(" and string[end_idx] == ")":
		return string[start_idx:end_idx+1]
	else:
		if string[start_idx] == "(":
			return parenBitHelper(string,start_idx,end_idx-1)
		elif string[end_idx] == ")":
			return parenBitHelper(string,start_idx+1,end_idx)
		else:
			return parenBitHelper(string,start_idx+1, end_idx-1)

print(parenBit("123(hello)abc"))

