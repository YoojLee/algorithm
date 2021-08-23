# 숫자 고르기
"""
문제 설명

세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다.
첫째 줄의 각 칸: 1~N
둘째 줄에는 1이상 N 이하인 정수가 랜덤하게 들어가 있음.

그래프 사이클 찾는 문제로 수렴됨. -> dfs?
"""

import sys
from collections import defaultdict

input = lambda:sys.stdin.readline()

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return


N = int(input().strip())
graph = defaultdict(list)

for i in range(1, N+1): # graph 생성
    v = int(input().strip())
    graph[v].append(i) # line2를 vertex로

checked = [0] * (N+1) # checked를 만들어서 탐색을 할 것인지 체크
result = []

for i in range(1, N+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for x in result:
    print(x)