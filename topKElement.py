def topKElement(nums, k):

	count = {} # create counter dict
	freq = [[] for i in range(len(nums)+1)] # convert 

	for n in nums:

		count[n] = 1 + count.get(n, 0)

	print(count)

	for n, c in count.items():
		freq[c].append(n)

	print(freq)

	res = []
	for i in range(len(freq)-1, -1, -1):
		
		for n in freq[i]:
			res.append(n)

			if len(res) == k:
				return res


nums = [1,1,1,2,2,3]
k = 2
# print(topKElement(nums, k))
print([[]for i in range(len(nums))])
