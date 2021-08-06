def solution(x, n):
    a = (1 if x>=0 else -1)    
    if x == 0:
        return [0]*n
    else:
        return [i for i in range(x, (x*n)+a, x)]
        