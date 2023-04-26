changes = [300, 60, 10] #5분 1분 10초
T = int(input())
res = []

for i in changes :
    res.append(T // i) #몫
    T = T % i	# 나머지
    
if(T != 0):
    print(-1)
else:
    print(*res)