def solution(a, b):
    answer = 0
    max_n = max(a,b)
    min_n = min(a,b)
    
    for i in range(min_n, max_n+1):
        answer += i
    
    return answer

new_id = 'asd-_.#$!@#'
if '-' not in ['-','_','.']:
    print('있')

