def solution(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    n = rev_base[::-1] 
    n = n[::-1]
    n = int(n,3)
    return n