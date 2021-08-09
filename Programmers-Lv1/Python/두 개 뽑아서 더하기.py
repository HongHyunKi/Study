def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if i == j:
                pass
            else:
                answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer
    