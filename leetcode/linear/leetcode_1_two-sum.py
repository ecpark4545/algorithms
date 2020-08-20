"""
https://leetcode.com/problems/two-sum/

Problem
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
	def twoSum_1(self, nums: List[int], target: int) -> List[int]:
		'''
		Brute-Force
		'''
		num_len = len(nums)
		for i in range(num_len):
			for j in range(i + 1, num_len):
				if nums[i] + num[j] == target:
					return [i, j]
				
	def twoSum_2(self, nums: List[int], target: int) -> List[int]:
		'''
		In
		'''
		for i, n in enumerate(nums):
			second = target - n
			if second in nums[i + 1:]:
				return [i, nums[i + 1:].index(second) + i + 1]
			
	def twoSum_3(self, nums: List[int], target: int) -> List[int]:
		'''
		Dictionary 2 loop
		'''
		pair_nums={}
		for i, num in enumerate(nums):
			pair_nums[num] = i
			
		for i, num in enumerate(nums):
			if target-num in pair_nums and i != pair_nums[target-num]:
				return [nums.index(num), pair_nums[target-num]]
				
	def twoSum_4(self, nums: List[int], target: int) -> List[int]:
		'''
		Dictionary 1 loop
		'''
		pair_nums = {}
		for i, num in enumerate(nums):
			if target - num in pair_nums:
				return [pair_nums[target-num], i]
			pair_nums[num] = i
