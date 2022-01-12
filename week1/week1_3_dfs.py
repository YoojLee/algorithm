# floodfill dfs 풀이
def solution(n, m, image):
    answer = 0
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(y, x, cur_area):

        if (y < 0 or y >= n) or (x < 0 or x >= m):
            return

        if visited[y][x]:
            return 

        if image[y][x] != cur_area:
            return
        
        visited[y][x] = True
        dfs(y-1, x, image[y][x]) # 상
        dfs(y+1, x, image[y][x]) # 하
        dfs(y, x-1, image[y][x]) # 좌
        dfs(y, x+1, image[y][x]) # 우
    
    for py in range(n):
        for px in range(m):
            if visited[py][px]:
                continue

            dfs(py, px, image[py][px])

            answer += 1

    return answer