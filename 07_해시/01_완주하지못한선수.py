def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1 :
            return participant[i]
        elif participant[i] != completion[i] :
            return participant[i]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))