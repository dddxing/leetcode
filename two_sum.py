def two_sum(nums, target):

	dict_ = {}

	for idx, item in enumerate(nums):

		diff = target - item
		print(diff)
		if diff not in dict_:
			dict_[item] = idx
			
		else:
			return dict_[diff], idx
			




nums = [11, 15, 2, 7]
target = 9
print(two_sum(nums, target))
