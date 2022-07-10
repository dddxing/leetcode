def two_sum_2(nums, target):
	"""
	sorted input array
	"""
	pass

	l, r = 0, len(nums) - 1
	while l < r:
		cursum = nums[l] + nums[r]

		if cursum > target:
			r -= 1

		elif cursum < target:
			l += 1
		else:
			return l+1, r+1

nums = [2, 7, 11, 15]
target = 9

print(two_sum_2(nums, target))