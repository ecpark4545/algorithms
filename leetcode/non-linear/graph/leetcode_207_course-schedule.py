'''
https://leetcode.com/problems/course-schedule/
https://leetcode.com/problems/course-schedule/discuss/658379/Python-by-DFS-and-cycle-detection-w-Graph
https://blog.csdn.net/fuxuemingzhu/article/details/82951771
https://www.pymoon.com/entry/207-Course-Schedule
Problem
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
             
             
Hint1 : This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
'''
from collections import defaultdict


class Solution:
	def canFinish(self, numCourses, prerequisites):
		graph = defaultdict(list)
		for now, before in prerequisites:
			graph[now].append(before)
			
		def dfs(course):
			if checker[course] == 1:
				return True
			elif checker[course] == 2:
				return False
			# init as 1
			checker[course] = 1
			for pre_course in graph[course]:
				if dfs(pre_course):
					return True
			checker[course] = 2
		
		checker = [0 for i in range(numCourses)]
		for course in range(numCourses):
			if dfs(course):
				return False
		
		return True
n=2
pre = [[1,0],[0,1]]
s=Solution()
s.canFinish(numCourses=n,prerequisites=pre)
