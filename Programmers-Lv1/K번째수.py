def solution(arr, commands):
    answer = []
    temp = []
    t = []
    
    for i, j, k in commands:
        temp.append(sorted(arr[i-1:j]))
        t.append(k)
    for i in range(0, len(t)):
        answer.append(temp[i][t[i]-1])

    return answer