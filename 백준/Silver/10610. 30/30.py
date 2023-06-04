n = list(map(int,input()))
n.sort(reverse=True)
sum = 0
for i in n:
    sum += i

# 1. 각 자리의 숫자가 3으로 나누어 떨어져야한다.
# 2. 일의 자리는 0이어야 한다.
if sum % 3 != 0 or 0 not in n:
    print(-1)
else:
    for i in n:
        print(i, end="")