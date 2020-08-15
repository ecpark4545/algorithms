"""
https://leetcode.com/problems/valid-palindrome/

Problem
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
"""

import re
from collections import deque

class Solution:
	def isPalindrome_1(self, s: str) -> bool:
		'''
		use List(pop) and isalnum()
		'''
		strs = []
		for char in s:
			if char.isalnum():
				strs.append(char.lower())
			
			while len(strs) > 1:
				if strs.pop(0) != strs.pop():
					return False
			return True
	
	def isPalindrome_2(self, s: str) -> bool:
		'''
		use deque(popleft) and isalnum()
		'''
		strs = deque()
		for char in s:
			if char.isalnum():
				strs.append(char.lower())
		
		while len(strs) > 1:
			if strs.popleft() != strs.pop():
				return False
		return True
	
	def isPalindrome_3(self, s: str) -> bool:
		'''
		use regex and Slicing
		'''
		s = s.lower()
		s = re.sub('[^a-z0-9]','', s)
		return s == s[::-1]
