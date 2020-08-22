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
import sys
from heapq import *

input = sys.stdin.readline

'''
Prim algorithm
- 1. initialize graph information
- 2. random setting starting node (weight:0, start: 1)
- 3. put adj nodes into candidate, then pop smallest weights (priority queue, heapq)

'''


def prim(num_vertex, graph):
    mst = 0
    # 1
    edges = [[] for _ in range(num_vertex + 1)]
    checked = [False for _ in range(num_vertex + 1)]
    for n1, n2, w in graph:
        edges[n1].append((w, n2))
        edges[n2].append((w, n1))
    # 2
    candidate = [(0, 1)]  # weight, start_node
    while candidate:
        w, n1 = heappop(candidate)
        if checked[n1]:
            continue
        checked[n1] = True
        mst += w
        # 3
        for w, n2 in edges[n1]:
            if checked[n2]:
                continue
            heappush(candidate, (w, n2))
    print(mst)


if __name__ == "__main__":
    num_vertex, edges = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(edges)]
    prim(num_vertex, graph)
