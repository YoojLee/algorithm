# 방문 길이 (lv.3)
from collections import defaultdict
def solution(dirs):
    """
    공간 -> 10x10 2-D array (이걸 직접적으로 구현하는 것보단 좌표로 하는 게 더 빠를 것 같음)
    
    initial 좌표를 (0,0)으로 해놓고 움직이는 방향이 어떨까
    
    그리고 dirs는 dictionary 키값으로 지정해놓는 거지!!!
    
    캐릭터가 처음 걸어본 길의 길이 -> 라고 하면 어쨌든 여기를 방문했는지 안했는지를 알아야하는 건데 그러면 visited를 만들어두고 set 등으로 지정해놔야할 것 같음. 아니면 아예 set으로 해놓고 탐색을 하는 방향도 나쁘진 않을 것 같음.
    
    """
    answer = len(dirs)
    prev_pt = (0,0) # 시작 지점
    dir_dict = {"U": (1,0), "D": (-1,0), "R": (0,1), "L": (0,-1)}
    visited = defaultdict(set)
    
    for i, d in enumerate(dirs):
        new_pt = tuple(map(lambda x: x[0]+x[1], zip(prev_pt, dir_dict[d])))
        
        if (-5 <= new_pt[0] <= 5) and (-5 <= new_pt[1] <= 5):
            if new_pt in visited[prev_pt] or prev_pt in visited[new_pt]:
                answer -= 1
            else:
                visited[prev_pt].add(new_pt)
                visited[new_pt].add(prev_pt)
            prev_pt = new_pt
        else:
            answer -=1


    return answer


if __name__ == "__main__":
    #dirs = "ULURRDLLU"
    dirs = "LULLLLLLU"
    answer = solution(dirs)
    print(answer)