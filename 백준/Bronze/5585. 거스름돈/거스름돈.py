changes = [500, 100, 50, 10, 5, 1] #엔화
T = int(input())
pay = 1000 - T
cnt = 0

for i in changes :
    cnt += pay // i
    pay %= i

print(cnt)