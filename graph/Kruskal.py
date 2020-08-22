# Spanning Tree
# 1. All nodes connected
# 2. No cycle

'''
Kruskal's algorithm - edge
Union-Find algorithm
union-by-rank, path compression
'''

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
  # path compression
  if parent[node]!=node:
    parent[node] = find(parent[node])
  return parent[node]

def union(n1,n2):
  root1=find(n1)
  root2=find(n2)

  # union-by-rank
  if rank[root1] > rank[root2]:
    parent[root2] = root1
  else:
    parent[root1] = root2
    if rank[root1] == rank[root2]:
      rank[root2]+=1


def make_set(node):
  parent[node]=node
  rank[node]=0

def kruskal(graph):
  mst=[]
  # 1. init
  for node in graph['vertices']:
    make_set(node)

  # 2. weigth sort
  edges = graph['edges']
  edges.sort()

  # 3. connect (no cycle)
  for edge in edges:
    w, n1, n2 = edge
    if find(n1)!=find(n2):
      union(n1,n2)
      mst.append(edge)
  print(mst)



kruskal(graph)