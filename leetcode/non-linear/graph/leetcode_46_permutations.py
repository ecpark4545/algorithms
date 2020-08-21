"""
https://leetcode.com/problems/permutations/

Problem
Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import itertools
class Solution_1:
	def permute(self, nums: List[int]) -> List[List[int]]:
		result = []
		cash=[]
		def dfs(source):
			if len(source) == 0:
				result.append(cash[:])
				
			for e in source:
				next_source = source[:]
				next_source.remove(e)
				cash.append(e)
				dfs(next_source)
				cash.pop()
		dfs(nums)
		return result
	
class Solution_2:
	def permute(self, nums: List[int]) -> List[List[int]]:
		return list(itertools.permutations(nums))