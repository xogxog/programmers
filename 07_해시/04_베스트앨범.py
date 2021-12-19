def solution(genres, plays):
    playlist={}
    for i in range(len(genres)):
        if genres[i] in playlist.keys():
            # print(playlist[genres[i]][0])
            playlist[genres[i]][0] += plays[i]
            playlist[genres[i]][1].append(i)

        else:
            playlist[genres[i]] = [plays[i],[i]]
    print(playlist)
    answer = []
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))