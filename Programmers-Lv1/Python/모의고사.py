def solution(answer):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [[1, 0], [2, 0], [3, 0]] 

    for i in range(0,len(answer)):
        if answer[i] == supo_1[i%5]:
            score[0][1] += 1
        if answer[i] == supo_2[i%8]:
            score[1][1] += 1
        if answer[i] == supo_3[i%10]:
            score[2][1] += 1
    
    result = []
    for i in range(3):
        if max(score, key = lambda x : x[1])[1] == score[i][1]: 
            result.append(i+1)
    return result