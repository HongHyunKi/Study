def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        temp = ''
        for j in range(0,len(i)):
            if j % 2 == 0:
                temp += i[j].upper()
            else:
                temp += i[j].lower()
        answer.append(temp)
    return ' '.join(answer)