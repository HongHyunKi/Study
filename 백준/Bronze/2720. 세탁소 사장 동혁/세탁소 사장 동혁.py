changes = [25, 10, 5, 1] #쿼터, 다임, 니켈, 페니
T = int(input())

for _ in range(T) :
    C = int(input())
    res = []

    for i in changes :
        res.append(C // i) #몫
        C = C % i	# 나머지 C에 할당
        
    print(*res)