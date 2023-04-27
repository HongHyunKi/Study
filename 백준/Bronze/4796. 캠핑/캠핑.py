cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    
    res = (V // P) * L    
    V = V % P
    
    if V <= L:
        res += V
    else:
        res += L
    
    print("Case {0}: {1}".format(cnt, res))
    cnt += 1
