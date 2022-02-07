# Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".


# stringClean("yyzzza") → "yza"
# stringClean("abbbcdd") → "abcd"
# stringClean("Hello") → "Helo"


def stringClean(string):
	if len(string) == 1:
		return string
	else:
		if (string[0]==string[1]):
			return stringClean(string[1:])
		else:
			return string[0] + stringClean(string[1:])

print(stringClean('aabbbcccddddwxxyzzz'))