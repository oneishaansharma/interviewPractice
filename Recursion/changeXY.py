# Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.


# changeXY("codex") → "codey"
# changeXY("xxhixx") → "yyhiyy"
# changeXY("xhixhix") → "yhiyhiy"


def changeXY(string):
	if string == '': return ''
	if string[-1] == 'x': return changeXY(string[:-1]) + 'y'
	else:
		return changeXY(string[:-1]) + string[-1]

res = changeXY('xhixhixthisisasexystring')

print(res)
