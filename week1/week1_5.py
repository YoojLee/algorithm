import heapq

def solution(no, works):
    """
    배상비용 최소화
    
    배상비용 = work_left의 제곱합
    -> max-heap
    
    """    
    result = 0
    works = [-work for work in works] # max heap 구성을 위함.
    heapq.heapify(works)
    
    while no:
        max_work = heapq.heappop(works)
        max_work += 1
        no -= 1
        
        heapq.heappush(works, max_work)
    
    result = sum(work**2 for work in works)

    return result

if __name__ == "__main__":
    works = [4,3,3]
    no = 4
    
    res = solution(no, works)
    print(res)