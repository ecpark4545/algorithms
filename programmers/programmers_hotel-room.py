'''
https://programmers.co.kr/learn/courses/30/lessons/64063
'''


def solution_1(k, room_number):
	answer = []
	reserved_dict = defaultdict(int)
	
	for want in room_number:
		if want not in reserved_dict:
			reserved_dict[want] = want + 1
			answer.append(want)
		else:
			count = 1
			while reserved_dict[want + count] != 0:
				count += 1
			# 내가 방문했던 노드들의 부모노드 업데이트
			for i in range(want, want + count + 1):
				reserved_dict[i] = want + count + 1
			# 이번 방문 노드 추가
			answer.append(want + count)
	return answer


from collections import defaultdict


def solution_2(k, room_number):
	answer = []
	reserved_dict = defaultdict(int)
	
	for want in room_number:
		current_room = find(want, reserved_dict)
		answer.append(current_room)
	
	return answer


def find(target, rooms):
	# 만약 target이 빈방이면 바아로 rooms에 추가하고 손절(==return)
	if target not in rooms:
		rooms[target] = target + 1
		return target
	
	# 만약 target이 이미 누가 예약했어? 그럼 적어도 그놈의 부모노드를 새 target으로 변경하고 들어가
	#   ->고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
	# rooms[target] == 이미 예약당한 방의 부모노드 값
	rooms[target] = find(rooms[target], rooms)
	return rooms[target]



k = 10
room_number = [1, 3, 4, 1, 3, 1]
s_1 = solution_1(k, room_number)
s_2 = solution_2(k, room_number)




