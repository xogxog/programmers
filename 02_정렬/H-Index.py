# def solution(citations):
#     citations.sort()
#     print(citations)
#     idx = 0
#     for i in range(len(citations)-1,-1,-1):
#         if citations[i] <= len(citations)-i and citations[i] >= i :
#             print(f'i : {i},{citations[i]}:번 이상 인용된 논문 - {len(citations)-i }, 이하 : {i}')
#             idx = i
#             return citations[idx]

def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        print(f'{citations[i]} : {article_count - i}')
        if citations[i] >= article_count - i:
            print(i)
            return article_count - i
    return 0




print(solution([3, 0, 6, 1,1,3, 5]))
print(solution([1,1,1,1,1,1,1,1000]))