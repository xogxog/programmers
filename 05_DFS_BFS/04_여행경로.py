def solution(tickets):
    visited = [0] * len(tickets)
    tmp =[]
    answer = ["ICN"]
    idx = 0
    # Z의 아스키 코드

    while sum(visited) != len(visited) :
        min_ord = 90
        for i in range(len(tickets)) :
            if not visited[i] and tickets[i][0] == answer[-1] :
                if ord(tickets[i][1][0]) < min_ord :
                    min_ord = ord(tickets[i][1][0])
                    idx = i
        visited[idx] = 1
        answer.append(tickets[idx][1])


    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))