# Recursion-1 > array6

# Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


# array6([1, 6, 4], 0) → true
# array6([1, 4], 0) → false
# array6([6], 0) → true


def array6(array):
	return array6helper(array,0)

def array6helper(array, idx):
	if (idx <= len(array)-1):
		if (int(array[idx]) == 6):
			return True
		else:
			return array6helper(array,idx+1)
	return False


res = array6(['1','6','4'])

print(res)