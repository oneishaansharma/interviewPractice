# Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".


# changePi("xpix") → "x3.14x"
# changePi("pipi") → "3.143.14"
# changePi("pip") → "3.14p"


def changePi(string):
	if len(string)<2:
		return string
	if string[0:2] == 'pi':
		return '3.14' + changePi(string[2:])
	else:
		return string[0] + changePi(string[1:])


res = changePi('xpixpixpix')
print(res)