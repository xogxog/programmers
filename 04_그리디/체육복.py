def solution(n, lost, reserve):
    
    # clothes = [1] * (n+1)

    # 런타임에러
    # for i in range(1,len(clothes)+1):
    #     if i in lost :
    #         clothes[i] -= 1
    #     if i in reserve :
    #         clothes[i] += 1

    #런타임에러
    # print(clothes)
    # # 도난
    # for i in range(len(lost)) :
    #     clothes[lost[i]] -=1

    # # 체육복남는애
    # for i in range(len(reserve)) :
    #     clothes[reserve[i]] += 1
    
    # answer = 0
    # for i in range(1,len(clothes)): # 학생번호1부터 시작이므로 0번인덱스 버림
    #     if clothes[i] <1:
    #         if clothes[i-1] >=2 :
    #             clothes[i] +=1
    #             clothes[i-1] -=1
    #         elif clothes[i+1]>=2 :
    #             clothes[i] +=1
    #             clothes[i+1] -=1
    #     if clothes[i] >=1 :
    #         answer+=1

    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost)-set(reserve)

    for i in set_reserve :
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
    return n-len(set_lost)


print(solution(5,[2,4,5],[1,3,5]))
print(solution(5,[2,4],[3]))