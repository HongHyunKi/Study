def solution(arr):
    if len(arr) == 0 or len(arr) == 1:
       return [-1]
    else:
        arr.remove(min(arr))
    return arr

a = [1,2,3,4]
b = [10]
print(solution(a))
print(solution(b))
