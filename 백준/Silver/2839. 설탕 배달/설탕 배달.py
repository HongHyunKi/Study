N = int(input())
cnt = 0

while N >= 0:
    #5로 나누어 떨어질 때 break
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    
    #3kg 봉투 한 개씩 빼기
    N -= 3
    cnt += 1

#루프가 '자연적'으로 끝나는 경우 실행
else:
    print(-1)