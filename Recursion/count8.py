# Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


# count8(8) → 1
# count8(818) → 2
# count8(8818) → 4

def count8(number):
	if int(number/10) == 0:
		if number == 8:
			return 1
		else:
			return 0
	else:
		if(number%10 == 8 and int(number/10)%10 == 8):
			return 2 + count8(int(number/10))
		elif(number%10 == 8):
			return 1 + count8(int(number/10))
		else:
			return count8(int(number/10))


print(count8(88818188))
