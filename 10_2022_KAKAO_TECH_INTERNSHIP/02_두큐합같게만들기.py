from collections import deque
def solution(queue1, queue2):
    global tot, cnt
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot = (sum(queue1)+sum(queue2)) // 2
    q1_sum = sum(queue1)
    cnt = 0
    max_cnt = len(q1)*2 + len(q2)

    while 1 :
        if q1_sum == tot :
            return cnt
        if not len(q1) or not len(q2) or cnt > max_cnt :
            return -1
        elif q1_sum < tot :
            q2_tmp=q2.popleft()
            q1_sum += q2_tmp
            q1.append(q2_tmp)
            cnt += 1
        else :
            q1_tmp = q1.popleft()
            q1_sum -=q1_tmp
            q2.append(q1_tmp)
            cnt += 1

    return -1

solution([3,2,7,2],[4,6,5,1])