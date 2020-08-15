"""
https://leetcode.com/problems/most-common-word/

Problem
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.
The answer is in lowercase.



Example 1:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

Output: "ball"

Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.

Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

from collections import Counter as C
from collections import defaultdict as D

class Solution:
	def mostCommonWord_1(self, paragraph: str, banned: List[str]) -> str:
		"""
		1. use regex: substutute any character which is not word with space
		2. defaultdict and max
		"""
		words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
			.lower().split()
						 if word not in banned]
		
		counts = D(int)
		for word in words:
			counts[word]+=1
		
		return max(counts,key=counts.get)
	
	def mostCommonWord_2(self, paragraph: str, banned: List[str]) -> str:
		"""
		1. use regex: substutute any character which is not word with space
		2. Counter.most_common
		"""
		words= [word for word in re.sub(r'[^\w]',' ',paragraph)
			.lower().split()
						if word not in banned]
		
		counts=C(words)
		return counts.most_common(1)[0][0]