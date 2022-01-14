# 야근 지수
import heapq

def solution(n, works):
    """
    max heap 구현
    """
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    
    while n and heap[0] < 0:
        item = heap[0]+1
        heapq.heapreplace(heap, item)
        n -= 1
    
    answer = sum(work**2 for work in heap)
    return answer