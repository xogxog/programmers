# 	N = 5
#	arr1 = [9, 20, 28, 18, 11]
#   arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):

    map1 = MyBin(n,arr1)
    map2 = MyBin(n,arr2)
    answer = [""]*n

    for i in range(n) :
        for j in range(n) :
            if map1[i][j] == '0' and map2[i][j] == '0' : #둘다 0인 경우에만 공백
                answer[i] += " "
            else : # 그 이외에는 # 채워줌.
                answer[i] += '#'


    return answer




def MyBin(n,arr) :
    ls = [] # 2진수로 바꾼 문자열 받을 리스트변수
    # print(arr)
    for i in range(n):
        mybin = "" # 2진수로만든 문자열 받음
        num = arr[i] # 10진수 수를 따로 저장
        # 2진수로 바꾸는 반복문
        while num >= 1:
            mybin = str(num % 2) + mybin
            num //= 2

        # 길이를 n만큼 채워야 하므로 n보다 짧게 나온 문자열을 짧은 만큼의 0을 앞에 붙인다.
        if len(mybin) < n:
            mybin = (str(0) * (n - len(mybin))) + mybin
        ls.append(mybin)


    return ls




arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
map = solution(5,arr1,arr2)

print(map)
