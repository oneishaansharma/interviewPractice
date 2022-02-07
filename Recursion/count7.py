# Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


# count7(717) → 2
# count7(7) → 1
# count7(123) → 0


def count7(num):
	if(int(num/10)==0):
		if num==7:
			return 1
		else:
			return 0
	else:
		if(num%10 == 7):
			return 1+count7(int(num/10))
		else:
			return count7(int(num/10))



print(count7(73777))
