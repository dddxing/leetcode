import unittest
import pytest
from collections import defaultdict

def buystock(nums):
	pass



def two_sum(nums, target):
	pass

def productExceptSelf(nums):
	pass

def maxSubArray(nums):
	pass


def maxSubArrayProd(nums):
	cur_max, cur_min = 1, 1
	res = nums[0]

	for i in ranage(1, len(nums)):
		if n == 0:
			cur_max, cur_min = 1, 1
			continue
		tmp = cur_max * n
		cur_max = max(tmp, cur_min * n, n)
		cur_min = min(tmp, cur_min * n, n)


def findMinRotSort(nums):
	"""
	find min in rotated sorted array
	"""
	pass


def two_sum_2(nums, target):
	"""
	sorted input array
	"""
	pass

def three_sum(nums, target):
	pass


def maxWaterArea(nums):
	pass


def group_anagrams(strs):
	pass

def main():

	nums1 = [7, 1, 5, 3, 6, 4]
	nums2 = [2, 7, 11, 15]
	target1 = 9
	target2 = 0

	nums3 = [1,2,3,4]
	nums4 = [5, 4, -1, 7, 8]
	nums5 = [2, 3, -2, 4]
	nums6 = [3, 4, 5, 1, 2]
	nums7 = [-1,0,1,2,-1,-4]
	nums8 = [1,8,6,2,5,4,8,3,7]
	strs = ["eat","tea","tan","ate","nat","bat"]


	print(buystock(nums1))
	print(two_sum(nums2, target1))
	print(productExceptSelf(nums3))
	print(maxSubArray(nums4))
	print(maxSubArrayProd(nums5))
	print(findMinRotSort(nums6))
	print(two_sum_2(nums2, target1))
	print((three_sum(nums7, target2)))
	print(maxWaterArea(nums8))
	print(group_anagrams(strs))


if __name__ == "__main__":
	main()