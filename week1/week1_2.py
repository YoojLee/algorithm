# programmers level2. 기능 개발

from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    day_left = [ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]
    count = 0
    
    # queue로 해주기
    dq = deque(day_left)
    
    while dq:
        while dq[0] > 0:
            dq = deque(elem-1 for elem in dq)
        while dq and dq[0] <= 0: # dq를 추가해주지 않으면 deque index out of range error 발생
            dq.popleft()
            count += 1
            
        answer.append(count)
        count = 0
        
        
    return answer


if __name__ == "__main__":
    progresses = [93,30,55]
    speeds = [1,30,5]
    
    answer = solution(progresses, speeds)
    print(answer)