#프로그래밍1: [2022 상반기 대학 모의고사] 발판 밟고 벽 넘어가기_Lv1

def solution(h, k, boxes):
    temp = 0
    boxes = sorted(boxes)
    result = []
    
    while (temp+k) <= h:
        #종료조건
        if temp+k >= h:
            break
        
        #k보다 낮은 후보군
        cnd = []
        
        #점프할 수 있는 발판 cnd에 추가하기
        for i in boxes:
            if i <= temp+k:
                cnd.append(i)
            else:
                break
            
        #불필요한 반복 횟수 줄이기 위해 리스트 축소
        for _ in range(len(cnd)):
            boxes.pop(0)
        
        #k보다 낮으면서 가장 큰 값 result에 추가
        if cnd:
            result.append(max(cnd))
            temp = max(cnd)
        else: 
            return -1
        
    return len(result)

print(solution(20, 18, [1] ))
