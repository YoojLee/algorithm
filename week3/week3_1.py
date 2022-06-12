# 세 소수의 합

def solution(n):
    answer = 0
    
    def primary_numbers(n):
        """
        에라토스테스트의 체 알고리즘을 기반으로!
        """
        arr = [i+1 for i in range(1,n)]
        
        for i in range(2,n+1):
            for j in range(len(arr)):
                if arr[j] == 0:
                    continue
                if arr[j] != i and arr[j] % i == 0:
                    arr[j] = 0
                
        return [i for i in arr if i != 0]
    
    primary = primary_numbers(n)
    
    for i in range(len(primary)):
        for j in range(i,len(primary)):
            for k in range(j,len(primary)):
                if i == j or j == k or i == k:
                    continue
                if primary[i]+primary[j]+primary[k] == n:
                    answer += 1
        
    return answer