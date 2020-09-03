'''
https://programmers.co.kr/learn/courses/30/lessons/43164
'''
import heapq
from collections import defaultdict, deque

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def solution(tickets):
	path = defaultdict(list)
	for depart, arrive in tickets:
		heapq.heappush(path[depart], arrive)
	
	if not path:
		return []
	
	
	stack=['ICN']
	answer=deque()
	while stack:
		depart=stack[-1]
		
		if len(path[depart])==0:
			answer.appendleft(stack.pop())
		else:
			stack.append(heapq.heappop(path[depart]))
		
	return list(answer)
solution(tickets)


