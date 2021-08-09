def solution(n):
    answer = []
    n = str(n)
    for i in range(0, len(n)):
        answer.append(int(n[i]))
    answer.reverse()
    return answer

a = 152345
print(solution(a))

b = 12345
print(reversed(str(b)))

b = 12345
print(list(b))
