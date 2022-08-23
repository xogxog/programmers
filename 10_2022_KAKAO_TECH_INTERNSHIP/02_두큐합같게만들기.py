from collections import deque
import sys

def solution(queue1, queue2):
    global tot, cnt
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot = (sum(queue1)+sum(queue2)) // 2
    q1_sum = sum(queue1)
    cnt = 0


    return -1

solution([3,2,7,2],[4,6,5,1])