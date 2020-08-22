# Spanning Tree
# 1. All nodes connected
# 2. No cycle

'''
Prim's algorithm - Node
heapq
'''
from heapq import *
from collections import defaultdict
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node, edges):
  mst=[]
  # 1. adj information save
  adj_edges = defaultdict(list)
  for w, n1, n2 in edges:
    adj_edges[n1].append((w,n1,n2))
    adj_edges[n2].append((w, n1, n2))

  # 2. random start node - take minimum edge
  connected_node = set(start_node)
  candidates = adj_edges[start_node]
  heapify(candidates)

  while candidates:
    w, n1, n2 = heappop(candidates)
    if n2 not in connected_node:
      connected_node.add(n2)
      mst.append((w,n1,n2))
      # 3. add adjs connected selected n2 which is not in connected node
      for edge in adj_edges[n2]:
        if edge[2] not in connected_node:
          heappush(candidates, edge)
  print(mst)

prim("A",myedges)

