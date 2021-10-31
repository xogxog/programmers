from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    for i in range(len(truck_weights)):
        truck_weights[i] = [truck_weights[i],0]
    print(truck_weights)
    time = 1
    cross = deque(truck_weights.popleft())
    print(cross)
    sum(truck_weights)
    while cross :
        time += 1
        truck = truck_weights.popleft()
        print(sum(cross))



    answer = 0
    return answer


print(solution(2,10,[7,4,5,6]))