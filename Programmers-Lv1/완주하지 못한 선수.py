def solution(participant, completion):
    count = 0
    participant = sorted(participant)
    completion = sorted(completion)
    for i in completion:
        if participant[count]!=i:
            break;
        count+=1

    return participant[count]