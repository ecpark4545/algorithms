'''
기존작업 도중에 새로운 작업이 들어오면, 대기시간이 발생 
1) 대기시간 발생 조건 True -> 작업시간 짧은기준으로 heap 후 처리
2) 대기시간 발생 조건 False -> 바로 처리 
3) 대기시간 == (현재 작업이 끝날시간 - 새로운 작업이 들어온 시간)
'''
from heapq import heappop, heappush


def solution(jobs):
	jobs.sort(reverse=True)
	N = len(jobs)
	answer, check = 0, 0  # check는 현재 작업중인 놈이 끝나는 시간
	wait = []  # 대기조
	
	while jobs:
		while jobs and jobs[-1][0] <= check:  # 1)
			start, cost = jobs.pop()
			heappush(wait, (cost, start))
		
		if not wait:  # 2)
			start, cost = jobs.pop()
			heappush(wait, (cost, start))
			check = start
		
		cost, start = heappop(wait)
		check += cost
		answer += check - start
	
	while wait:
		cost, start = heappop(wait)
		check += cost
		answer += check - start
	
	return answer // N


test = [[0, 3], [1, 9], [2, 6]]
solution(test)            

