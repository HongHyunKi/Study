N, K = map(int, input().split())
A = []
answer = 0

cnt = 0
while cnt < N:
    A.append(int(input()))
    cnt += 1

A.sort(reverse=True)

for i in A:
    if i > K:
        continue
    
    if i <= K:
        answer += K // i
        K %= i

print(answer)