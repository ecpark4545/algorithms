'''
sort 1. name 2. play 3.index
'''
from collections import defaultdict


def solution(genres=['classic', 'pop', 'classic', 'pop', 'classic', 'pop'], plays=[500, 600, 150, 600, 800, 2500]):
	result = []
	queue = [i for i in enumerate(zip(genres, plays))]
	plays_genre = defaultdict(int)
	for idx, (info) in queue:
		# queue == i, (genre, plays)
		# info == genre, plays
		plays_genre[info[0]] += info[1]
	
	queue.sort(key=lambda x: (plays_genre[x[1][0]], x[1][1], -x[0]))
	
	# for counting
	plays_genre = plays_genre.fromkeys(plays_genre, 0)
	
	while queue:
		idx, info = queue.pop()
		plays_genre[info[0]] += 1
		if plays_genre[info[0]] < 3:
			result.append(idx)
	
	return result


solution()
