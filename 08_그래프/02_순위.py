def solution(n, results):
    answer = 0
    adj_arr = [[] for _ in range(n+1)]
    ranking = [0]*(n+1)
    for node1, node2 in results :
        adj_arr[node1].append((node2,'win'))
        adj_arr[node2].append((node1,'lose'))
    print(adj_arr)

    for i in range(len(adj_arr)):
        if len(adj_arr[i]) == n-1 :
            answer += 1
            count = 0
            for j in range(len(adj_arr[i])) :
                if adj_arr[i][j][1] == "lose" :
                    count +=1
            ranking[count+1] = i # 몇등인지 기록
    print(ranking)
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))