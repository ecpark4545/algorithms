graph = {
	1: [2, 3, 4],
	2: [5],
	3: [5],
	4: [],
	5: [6, 7],
	6: [],
	7: [3]
}


# 1 recursive dfs
def recursive_dfs(v, discovered=[]):
	discovered.append(v)
	for w in graph[v]:
		if not w in discovered:
			discovered = recursive_dfs(w, discovered)
	return discovered

# 2 stack dfs
def iterative_dfs(v):
	discovered=[]
	stack =[v]
	while stack:
		node = stack.pop()
		if node not in discovered:
			discovered.append(node)
			for w in graph[node]:
				stack.append(w)
	return discovered

# 3 queue
def iterative_bfs(v):
	discovered=[v]
	queue = [v]
	while queue:
		node = queue.pop(0)
		for w in graph[node]:
			if w not in discovered:
				discovered.append(w)
				queue.append(w)
	return discovered
	
print(recursive_dfs(1,[]))
print(iterative_dfs(1))
print(iterative_bfs(1))