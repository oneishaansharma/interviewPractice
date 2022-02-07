# Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


# array11([1, 2, 11], 0) → 1
# array11([11, 11], 0) → 2
# array11([1, 2, 3, 4], 0) → 0


def array11(array):
	return array11helper(array,0)

def array11helper(array, idx):
	if (idx<=len(array)-1):
		if(int(array[idx])==11):
			return 1 + array11helper(array,idx+1)
		else:
			return array11helper(array,idx+1)
	return 0


res = array11([11,12,11,13,11,14])

print(res)