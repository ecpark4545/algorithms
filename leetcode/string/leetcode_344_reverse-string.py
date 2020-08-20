"""
https://leetcode.com/problems/reverse-string/

Problem
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.


Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


class Solution:
	def reverseString_1(self, s: List[str]) -> None:
		"""
		two-point swap
		"""
		left, right = 0, len(s)-1
		while left < right:
			s[left], s[right] = s[right], s[left]
			left +=1
			right -=1
			
	def reverseString_2(self, s: List[str]) -> None:
		"""
		reverse
		"""
		s.reverse()
		
	def reverseString_3(self, s: List[str]) -> None:
		"""
		slicing
		"""
		# s = s[::-1] / space complexity
		s[:] = s[::-1]