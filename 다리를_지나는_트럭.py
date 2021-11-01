from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    for i in range(len(truck_weights)):
        truck_weights[i] = [truck_weights[i], 1] # [트럭무게, 위치]

    tot_time = 1                                # 모든 트럭이 건널때까지 걸리는 시간
    cross = deque([truck_weights.popleft()])  # 현재 다리위에 있는 트럭

    while cross:                                # 다 건널때까지
        tot_time += 1
        idx = 0                                  # 다리 지나는 트럭을 가리킬 변수
        while True :                             # 현재 다리를 지나는 트럭들의 위치 +1
            if cross[idx][1] == bridge_length: # 트럭이 다 건넜다면
                cross.popleft()                  # 다리에서 리스트 빼기
            else :                               # 아직 건너고 있다면
                cross[idx][1] += 1               # 위치 +1
                idx += 1                         # 다음 트럭 가리키기
            if idx == len(cross):                # 모든트럭 위치 옮겼다면
                break                            # 반복문 중지
        # print(f'time : {tot_time}, cross :{cross}')
        if truck_weights :
            truck = truck_weights[0]
            if sum(cross[i][0] for i in range(len(cross))) + truck[0] <= weight: # 다리위에 다른 트럭이 올 수 있다면
                truck = truck_weights.popleft()
                cross.append(truck)
                # print(f'time : {tot_time}, cross :{cross}')

    return tot_time

print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))