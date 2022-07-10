from collections import defaultdict

def group_anagrams(strs):

	res = defaultdict(list)

	for string in strs:

		count = [0] * 26

		for char in string:

			count[ord(char) - ord("a")] += 1

		res[tuple(count)].append(string)

	return res.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))