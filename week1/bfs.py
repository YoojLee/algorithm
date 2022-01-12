## bfs 구현하는 거 연습
from collections import deque
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
} # 유향 그래프

def bfs(start_v):
    """
    어디서 방문 체크하는 게 좋을지 잘 생각해보자

    Args:
        start_v (int): 시작 정점
    """
    visited = []
    Q = deque([start_v])
    
    while Q:
        v=Q.popleft()
        if v not in visited: # 방문되지 않았으면
            visited.append(v) # 방문되었다고 표시
            for w in graph[v]: # 해당 정점의 인접 정점 탐색
                if w not in visited:
                    Q.append(w)

    return visited
# 위에 처럼 구현해도 되는데 25~26라인이 굳이 필요없을 것임. 처음에 visited도 start_v 넣어주고 시작하고, 
# 그 다음에 아예 w check할 때부터 바로 visited에 append 시켜주는 형태로 ㄱㄱ

def bfs2(start_v):
    visited = [start_v]
    Q = deque([start_v])
    
    while Q:
        v = Q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                Q.append(w)

    return visited

# 중복되는 동작을 하는 문장을 합쳐줬더니 코드가 보다 간결해졌음.

if __name__ == "__main__":
    visited = bfs(1)
    visited2 = bfs2(1)
    print(*visited)
    print(*visited2)
                
            
    
    