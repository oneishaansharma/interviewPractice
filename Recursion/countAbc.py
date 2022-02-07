# Count recursively the total number of "abc" and "aba" substrings that appear in the given string.


# countAbc("abc") → 1
# countAbc("abcxxabc") → 2
# countAbc("abaxxaba") → 2


def countAbc(string):
	if len(string) < 3:
		return 0
	else:
		if(string[0:3]=="abc" or string[0:3] == "aba"):
			
			# to count 'ababa' as 2 check again on the 3rd letter
			# return 1 + countAbc(string[2:])

			return 1 + countAbc(string[3:])
		else:
			return countAbc(string[1:])

print(countAbc("abaxxababa"))