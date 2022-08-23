def solution(survey, choices):
    answer = ''
    ls = [0] * 4  # R,T // C,F // J,M // A,N - 기준 앞
    tmp = ['R', 'C', 'J', 'A']
    tmp_2 = ['T', 'F', 'M', 'N']
    idx = 0
    for choice in choices:
        print(survey[idx], choice)
        if choice == 4:
            pass
        elif choice < 4:
            if survey[idx][0] in 'RT':
                if survey[idx][0] == 'R':
                    ls[0] += 4 - choice
                else :
                    ls[0] += choice - 4
            elif survey[idx][0] in 'CF':
                if survey[idx][0] == 'C':
                    ls[1] += 4 - choice
                else :
                    ls[1] += choice -4

            elif survey[idx][0] in 'JM':
                if survey[idx][0] == 'J':
                    ls[2] += 4 - choice
                else :
                    ls[2] += choice - 4

            elif survey[idx][0] in 'AN':
                if survey[idx][0] == 'A':
                    ls[3] += 4 - choice
                else :
                    ls[3] += choice -4
        else:
            if survey[idx][0] in 'RT':
                if survey[idx][1] == 'R':
                    ls[0] += choice - 4
                else :
                    ls[0] += 4-choice
            elif survey[idx][0] in 'CF':
                if survey[idx][1] == 'C':
                    ls[1] += choice - 4
                else :
                    ls[1] += 4-choice

            elif survey[idx][0] in 'JM':
                if survey[idx][1] == 'J':
                    ls[2] += choice - 4
                else :
                    ls[2] += 4-choice

            elif survey[idx][0] in 'AN':
                if survey[idx][1] == 'A':
                    ls[3] += choice - 4
                else :
                    ls[3] += 4-choice
        idx += 1

    for l in range(len(ls)):
        if ls[l] >= 0:
            answer += tmp[l]
        else:
            answer += tmp_2[l]

    return answer

solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])