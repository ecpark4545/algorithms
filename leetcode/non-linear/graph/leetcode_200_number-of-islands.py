"""
https://leetcode.com/problems/number-of-islands/

Problem
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

 
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		def dfs(i, j):
			if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
				return
			
			grid[i][j] = False
			dfs(i + 1, j)
			dfs(i - 1, j)
			dfs(i, j + 1)
			dfs(i, j - 1)
		
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					dfs(i, j)
					count += 1
		return count
