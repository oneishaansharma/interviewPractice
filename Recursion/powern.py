# Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


# powerN(3, 1) → 3
# powerN(3, 2) → 9
# powerN(3, 3) → 27

def powerN(num,exp):
	if exp == 0:
		return 1
	elif(exp%2 == 0):
		return powerN(num,exp/2)*powerN(num,exp/2)
	else:
		return powerN(num,int(exp/2))*powerN(num,int(exp/2))*num


res = powerN(2,10)

print(res)