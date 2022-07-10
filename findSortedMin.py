def findSortMin(nums):
	res = nums[0]
	l, r = 0, len(nums) - 1

	while l <= r:

		# check if this is already sorted
		if nums[l] < nums[r]:
			res = min(nums[l], res)
			break

		m = (l + r) // 2
		res = min(nums[m], res)

		if nums[m] >= nums[l]:
			l = m + 1

		else:
			r = m - 1

	return res

nums = [3, 4, 5, 1, 2]

print(findSortMin(nums))