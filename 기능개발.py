def solution(progresses, speeds):
    answer = []
    work =[]
    # 배포까지 일해야하는 날짜 세어주기
    for i in range(len(progresses)) :
        cnt = 0
        while progresses[i] < 100 :
            progresses[i] += speeds[i]
            cnt += 1
        work.append(cnt)

    release = 0
    cnt2 = 1
    for i in range(1, len(work)) :
        if work[i] <= work[release] : # 그 전의 작업과 동일 or 일찍 작업이 끝났다면
            cnt2 +=1                  # 함께 release 하기위해 + 1
        else :
            release = i                 # release할 기준 재설정
            answer.append(cnt2)         # 배포
            cnt2 = 1                    # 배포갯수 초기화
    answer.append(cnt2)                 #
    return answer
