# 알고력, 코딩력,
# 필요한 알고력, 코딩력, 증가하는 알고력, 코딩력, 푸는데 걸리는 시간
def solution(alp, cop, problems):
    answer = 0
    max_alp = 0
    max_cop = 0
    for i in range(len(problems)):
        max_alp = max(problems[i][0], max_alp)
        max_cop = max(problems[i][1], max_cop)
    dp = [[987654321]*(max_cop+1) for _ in range(max_alp+1)]
    alp = min(alp,max_alp)
    cop = min(cop,max_cop)
    dp[alp][cop] = 0
    for k in range(alp,max_alp+1) :
        for l in range(cop, max_cop+1) :
            # 학습
            if k+1 <= max_alp :
                dp[k+1][l] = min(dp[k+1][l], dp[k][l]+1)
            if l+1 <= max_cop :
                dp[k][l+1] = min(dp[k][l+1], dp[k][l]+1)

            for a,c,plus_a,plus_c,cost in problems :
                if k >= a and l >= c : # 풀 수 있는 문제라면
                    row = k+plus_a
                    col = l+plus_c
                    # 획득하는 알고, 코딩력이 범위 밖으로 넘어가지 않도록
                    if k+plus_a > max_alp :
                        row = max_alp
                    if l+plus_c > max_cop :
                        col = max_cop
                    dp[row][col] = min(dp[row][col], dp[k][l]+cost)

    return dp[-1][-1]