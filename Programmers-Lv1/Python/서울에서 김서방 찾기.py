def solution(n):
    temp = []
    answer = []

    for i in str(n):
        temp.append(i)
    for i in temp:
        answer.append(int(i))
    
    return sum(answer)
    