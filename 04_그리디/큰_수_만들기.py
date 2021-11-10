def solution(number, k):
    number_list = list(map(int, number))
    cnt = 0
    i=0
    answer =''
    while cnt < k:
        compare_list = number_list[i+1:i+k-cnt+1]
        # print(number_list)
        # print(compare_list)
        if i == len(number_list)-1 :
            number_list = list(map(int, answer)).append(number_list[i:])
            i=0
        elif number_list[i] < max(compare_list) :
            number_list[i] = -1
            i+=1
            cnt += 1
        else : 
            answer += str(number_list[i])
            i+=1
    
    answer +=''.join(map(str,number_list[i:]))
    return answer


print(solution("4177252841", 4))
print(solution("1231234", 3))
print(solution("1924", 2))
