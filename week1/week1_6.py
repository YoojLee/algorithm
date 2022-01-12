# level 3. 게임아이템

from collections import deque
from heapq import heappush, heappop

def solution_no_heap(healths, items):
    """
    정렬 풀이 -> 비효율적
    """    
    answer = []
    n, m = len(healths), len(items)
    n_rot = 0
    
    items = sorted(enumerate(items), key = lambda x: x[1][0], reverse = True) 
    healths.sort()
    
    # items에서 max값부터 비교하고 그 다음에 healths는 작은 값부터 비교해줌.
    for h_idx in range(n):
        for i_idx in range(m):
            n_rot += 1
            if len(answer) == m:
                return sorted(answer)
            if items[i_idx] == None:
                continue
                
            if (healths[h_idx] - items[i_idx][1][1]) >= 100:
                answer.append(items[i_idx][0]+1)
                items[i_idx] = None
                break
    
    return sorted(answer)


def solution_heap(healths, items):
    """
    heap을 이용하여 효율성 개선.
    """
    answer, n_rot = [], 0
  
    healths.sort()
    items = deque(sorted([item[1], item[0], idx+1] for idx, item in enumerate(items)))
    heap = []
    
    for health in healths: # 적은 체력의 캐릭터부터 탐색
        while items: # 소모하는 체력이 적은 아이템부터 탐색
            n_rot += 1
            debuff, buff, idx = items[0]
            if health - debuff < 100: # 해당 아이템이 조건에 부합하지 않으면 더이상 아이템에 대한 탐색은 무의미하므로 다음 캐릭터로 넘어감.
                break
            else: # 해당 캐릭터가 해당 아이템 사용이 가능한 경우 (최소 체력 조건에 부합)
                items.popleft() # 이후의 캐릭터에서 해당 아이템에 대한 탐색을 할 필요가 없음 (무조건 조건에 부합할 수밖에 없기 때문에)
                heappush(heap, [-buff, idx]) # max heap
                
        if heap: # 해당 캐릭터가 사용 가능한 아이템이 존재할 경우
            _, idx = heappop(heap) # max heap에서 공격력이 최대인 아이템을 answer에 삽입함.
            answer.append(idx)
    
    print(n_rot)
    return sorted(answer)