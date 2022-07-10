def three_sum(nums, target):

	res = []
	nums.sort()

	for i in range(len(nums)):

		if i > 0 and nums[i-1] == nums[i]:
			continue

		l, r = i + 1, len(nums) - 1

		while l < r:

			s = nums[i] + nums[l] + nums[r]

			if s > target:
				r -= 1

			elif s < target:
				l += 1

			else:
				res.append([nums[i], nums[l], nums[r]])
				l += 1

				while nums[l] == nums[l-1] and l < r:
					l += 1
	return res


nums = [-1,0,1,2,-1,-4]

print(three_sum(nums, 0))


		