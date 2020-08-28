"""
https://programmers.co.kr/learn/courses/30/lessons/42861
1. union-find
2. kruskal

"""

def solution(n, costs):
	def find(n1, parent):
		if parent[n1] == n1:
			return n1
		parent[n1] = find(parent[n1], parent)
		return parent[n1]
	
	def union(n1, n2, parent, rank):
		# root가 다른 상황만 union
		root1 = find(n1, parent)
		root2 = find(n2, parent)
		
		if rank[root1] > rank[root2]:
			parent[root2] = root1
		else:
			parent[root1] = root2
			if rank[root1] == rank[root2]:
				rank[root2] += 1
	
	result = 0
	parent = {i: i for i in range(n)}
	rank = {i: 0 for i in range(n)}
	
	for n1, n2, w in sorted(costs, key=lambda x: x[2]):
		if find(n1, parent) != find(n2, parent):
			union(n1, n2, parent, rank)
			result += w
	
	return result