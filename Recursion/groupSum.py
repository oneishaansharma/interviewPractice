# Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at index start and continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the recursive calls progress down the array.


# groupSum(0, [2, 4, 8], 10) → true
# groupSum(0, [2, 4, 8], 14) → true
# groupSum(0, [2, 4, 8], 9) → false

# Hint:
# The base case is when start>=nums.length. In that case, return true if target==0. Otherwise, consider the element at nums[start]. The key idea is that there are only 2 possibilities -- nums[start] is chosen or it is not. Make one recursive call to see if a solution is possible if nums[start] is chosen (subtract nums[start] from target in that call). Make another recursive call to see if a solution is possible if nums[start] is not chosen. Return true if either of the two recursive calls returns true.

def groupSum(array, target, start_idx):
	if start_idx >= len (array):
		return target == 0
	else:
		return groupSum(array, target-array[start_idx], start_idx+1) or groupSum(array, target, start_idx+1)


res = groupSum([6,3, 4, 7], 14, 0)
print(res)