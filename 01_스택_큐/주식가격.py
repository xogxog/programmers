def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j]:       # 주식가격이 떨어지지않는경우
                if j == len(prices)-1 :           # 끝까지 떨어지지 않은경우
                    answer.append(j-i)         # 떨어지지않은 기간 append
            else :                             # 주식이 떨어졌다면
                answer.append(j-i)             # 떨어지지 않은 기간 append
                break
    answer.append(0)                            # 마지막 주식은 항상 0

    return answer


print(solution([1, 2, 3, 2, 3]))