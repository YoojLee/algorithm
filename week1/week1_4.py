# lv2_더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    
    if set(heap) == {0}:
        return -1
    
    heapq.heapify(heap)
    
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        
        least = heapq.heappop(heap)
        second_least = heapq.heappop(heap)

        new = least + 2*second_least
        answer += 1
        
        heapq.heappush(heap, new)
         
    return answer

if __name__ == "__main__":
    scoville = [1,2]
    K = 7
    
    answer = solution(scoville, K)
    print(answer)
    