# level3 전염병

from collections import deque

def solution(m, n, infests, vaccinateds):
    """
    mxn 2차원 0 배열을 만듦.
    infests 자리에다가는 1 넣어주고,
    vaccinateds 자리에는 -1을 넣어주면 됨. 
    --> 배열 초기화 완료
    굳이 room 배열을 안만들고 infests랑 vaccinateds만으로도 충분히 구현은 가능할 것 같다.
    -> 그렇게 하면 조건 체크할 때 O(n)이라서 시간적으로 비효율적임. 배열을 구현하는 게 더 효율적임.
    
    이 문제는 배열을 한 번만 탐색하면 되는 문제이므로, Queue를 하나 만들어서 차례로 infests 정점 삽입해주면 됨.
    answer를 언제 update할지의 문제임..레벨별로 기록이 되는 건 아니니까..
    지금이 몇번째 level인지 어떻게 기록하는지가 문제임.
    """
    answer = 0
    
    room = [[-1 for _ in range(n)] for _ in range(m)]
    
    for r,c in infests:
        room[r-1][c-1] = 1
    
    for r, c in vaccinateds:
        room[r-1][c-1] = 0
        
    Q = deque([[r-1,c-1,0] for r,c in infests])
    direction = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우 direction 정의
    
    while Q:
        r,c,lv = Q.popleft()
        
        for dr, dc in direction:
            nr, nc = r+dr, c+dc
            
            if 0 <= nr < m and 0 <= nc < n and room[nr][nc] == -1:
                room[nr][nc] = 1
                infests.append([nr,nc])
                Q.append([nr, nc, lv+1])
    
    
    if len(infests)+len(vaccinateds) != m*n:
        return -1
    
    """
    if sum(sum(room[i]) for i in range(m))+len(vaccinateds) != m*n:
        return -1 # 이 방법이 좀 더 효율적인 듯
    """ 
    
    answer = lv
    return answer