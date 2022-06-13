# 세 소수의 합

def solution(n):
    answer = 0
    
    def prime_numbers(n):
        """
        에라토스테네스의 체 알고리즘을 기반으로!
        """
        arr = [i for i in range(n+1)]
        
        for i in range(2,int(n**(1/2))+1):
            if arr[i] == 0:
                continue
            for j in range(i**2, len(arr), i):
                arr[j] = 0
                
        return [i for i in arr[2:] if arr[i]]
    
    prime = prime_numbers(n)
    
    for i in range(len(prime)):
        for j in range(i,len(prime)):
            for k in range(j,len(prime)):
                if i == j or j == k or i == k:
                    continue
                if prime[i]+prime[j]+prime[k] == n:
                    answer += 1
        
    return answer

if __name__ == "__main__":
    answer = solution(33)
    print(answer)