"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

1: None  2: abc 3: def
4: ghi   5: jkl 6: mno
7: pqrs  8: tuv 9: wxyz


Example 1:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		def dfs(index, path):
			if len(path) == len(digits):
				result.append(path)
				return
			
			for i in range(index, len(digits)):
				for j in dic[digits[i]]:
					dfs(i + 1, path + j)
		
		if not digits:
			return []
		
		dic = {'2': 'abc', "3": 'def', "4": 'ghi', "5": 'jkl',
			   "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
		result = []
		dfs(0, "")
		return result
