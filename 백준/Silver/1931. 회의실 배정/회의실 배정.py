N = int(input())
I = []
result = []

#N만큼 입력받기
for i in range(N):
    temp = list(map(int, input().split()))
    I.append(temp)

#그리디의 핵심은 정렬!
#회의 시작시간 정렬 후 회의 끝 시간 정렬 
I.sort(key = lambda x: x[0])
I.sort(key = lambda x: x[1])

#시작지점
cnt = 1
curr = I[0][1]

for j in range(1, len(I)):
    if I[j][0]  >= curr:
        cnt += 1
        curr = I[j][1]
        continue

print(cnt)

