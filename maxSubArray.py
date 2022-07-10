def maxSubArray(nums):
	
	max_sum = nums[0]
	cur_sum = max_sum

	for i in range(1, len(nums)):

		cur_sum = max(nums[i] + cur_sum, nums[i])
		max_sum = max(max_sum, cur_sum)

	return max_sum


nums = [5,4,-1,7,8]

print(maxSubArray(nums))