# priorities : [2, 1, 3, 2]
from collections import deque
def solution(priorities, location):
    priorities = deque(enumerate(priorities))                       # index 붙이기
    _, prioritiy = max(priorities, key=lambda x: x[1])              # 가장 우선순위가 높은 친구 설정
    cnt = 1                                                         # 프린트 횟수 맨처음 프린트 하는것 자체가 1이므로 1부터 시작
    answer = 0
    while True :
        doc = priorities.popleft()
        if doc[1] == prioritiy :                                    # 가장 최우선 순위문서라면
            if doc[0] == location :                                 # 내가 찾고자하는 그 문서인지 확인
                answer = cnt
                break
            else :                                                  # 아니라면 최우선문서이므로 뽑고
                cnt += 1                                            # 프린트 횟수 +1
                _, prioritiy = max(priorities, key=lambda x: x[1])  # 우선순위 다시 찾기
        elif doc[1] < prioritiy :                                   # 우선순위보다 낮다면
            priorities.append(doc)                                  # 뒤로 보내기

    return answer



print(solution([2, 1, 3, 2],2))