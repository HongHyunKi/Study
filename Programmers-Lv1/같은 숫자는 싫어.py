def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if len(answer) ==0:
            answer.append(arr[i])
        
        if arr[i+1] is not None:
            if arr[i] != arr[i+1]:
                answer.append(arr[i+1])
        
    return answer