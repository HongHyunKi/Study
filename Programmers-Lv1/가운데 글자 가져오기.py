def solution(s):
    mid = int(len(s) / 2)
    
    if len(s) % 2 == 0:
        answer = s[mid-1] + s[mid]
    else:
        answer = s[mid]
    return answer