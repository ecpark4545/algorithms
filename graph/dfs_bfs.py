# DFS: Stack and Queue
# BFS: 2 Queues
from collections import deque
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start_node):
  visited, need_visit = [], []
  need_visit.append(start_node)

  while need_visit:
    node = need_visit.pop()
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])
  print(visited)


def bfs(graph, start_node):
  visited, need_visit = deque(), deque()
  need_visit.append(start_node)

  while need_visit:
    node = need_visit.popleft()
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])
  print(visited)

dfs(graph,'A')
bfs(graph,'A')