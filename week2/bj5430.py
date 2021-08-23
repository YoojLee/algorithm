# 5430. AC
"""
함수는 popleft (큐 구조)
"""
import sys
from collections import deque

input = lambda: sys.stdin.readline()
T = int(input().strip())

for t in range(T):
    cmds = deque(input().strip())
    N = int(input().strip())
    if N>0:
        arr = deque(map(int, input().replace("[","").replace("]","").split(",")))
    else:
        arr = []
    is_err = False
    # 명령어 처리
    while cmds:
        cmd = cmds.popleft()
        if cmd == "R":
            arr.reverse()
        else:
            try:
                arr.popleft()
            except:
                is_err = True
                break

    if is_err:
        print('error')
    else:
        print(list(arr))
    
    
    


