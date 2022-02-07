# Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.


# nestParen("(())") → true
# nestParen("((()))") → true
# nestParen("(((x))") → false


def nestParen(string):
	if len(string)==0: return True
	if len(string)==1: return False
	if string[0]=="(" and string[-1] ==")": return nestParen(string[1:-1])
	return False


string = "(((x)))"
print(nestParen(string))