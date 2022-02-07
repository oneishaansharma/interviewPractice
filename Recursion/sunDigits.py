
# Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


# sumDigits(126) → 9
# sumDigits(49) → 13
# sumDigits(12) → 3


def sumDigits(n):
	if (int(n/10) == 0):
		return n
	else:
		return n%10 + sumDigits(int(n/10))

print(sumDigits(9999))
