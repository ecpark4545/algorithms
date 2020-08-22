"""
BeakJoon 1197
https://www.acmicpc.net/problem/1197

Input:
3 3    <- # of Vertex and Edge
1 2 1  <- n1, n2, w
2 3 2  <- n1, n2, w
1 3 3  <- n1, n2, w

Output:
3      <- mst's weight
"""

'''
Kruskal's algorithm - edge
parent, rank lists to use union-find algorithm

1. init graph 
2. find minimum weight edge 
3. union-find
  3-1. path compression
  3-2. union-by-rank
'''

import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline

parent = dict()
rank = defaultdict(int)

# 3-1
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]  # return root
# 3-2
def union(n1, n2):
    root1, root2 = find(n1), find(n2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(nodes, graph):
    # 1
    mst = 0
    num_nodes = len(nodes)
    for n in range(1, num_nodes + 1):
        parent[n] = n

    # 2
    graph.sort()

    for edge in graph:
        w, n1, n2 = edge
        # 3
        if find(n1) != find(n2):
            union(n1, n2)
            mst += w
    print(mst)


if __name__ == "__main__":
    num_vertex, edges = map(int, input().split())
    nodes = set()
    graph = []
    for _ in range(edges):
        n1, n2, w = map(int, input().split())
        nodes.add(n1)
        nodes.add(n2)
        graph.append((w, n1, n2))
        graph.append((w, n2, n1))
    kruskal(nodes,graph)
