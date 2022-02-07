# Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


# array220([1, 2, 20], 0) → true
# array220([3, 30], 0) → true
# array220([3], 0) → false


def array220(array, idx):
	if(len(array)<2): return False
	if (idx>=len(array)-1):
		return False
	else:
		if(array[idx]*10 == array[idx+1]):
			return True
		else:
			return array220(array,idx+1)

res = array220([2,1,2,20,3,3],0)
print(res)
