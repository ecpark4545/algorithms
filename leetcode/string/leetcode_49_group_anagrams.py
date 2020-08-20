"""
https://leetcode.com/problems/group-anagrams/

Problem
Given an array of strings, group anagrams together.

Example 1:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
	- All inputs will be in lowercase.
	- The order of your output does not matter.
"""

from collections import defaultdict

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		'''
		use dictionary and sorted
		1. dictionary key = ''.join(sorted(word))
		2. dictionary value = word
		'''
		anagrams = defaultdict(list)
		for word in strs:
			anagrams[''.join(sorted(word))].append(word)
		return anagrams.values()
		
