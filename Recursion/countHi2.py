# Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.


# countHi2("ahixhi") → 1
# countHi2("ahibhi") → 2
# countHi2("xhixhi") → 0


def countHi(string):
	if len(string) < 2:
		return 0
	else:
		if string[0] == 'x':
			if string[1:3] == 'hi':
				return countHi(string[3:])
			else:
				return countHi(string[1:])
		else:
			if string[0:2] == "hi":
				return 1 + countHi(string[2:])
			else:
				return countHi(string[1:])

print(countHi('ahibhixhichidhixhi'))