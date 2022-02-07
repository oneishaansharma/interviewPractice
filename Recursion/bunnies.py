# We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).


# bunnyEars(0) → 0
# bunnyEars(1) → 2
# bunnyEars(2) → 4

def bunnies(numbuns):
	if numbuns == 0:
		return 0
	if numbuns == 1:
		return 2
	else:
		return 2+bunnies(numbuns-1)


print(bunnies(5))
