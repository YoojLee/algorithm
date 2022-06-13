# 약간 이해 못한 듯?...
import math
def solution(n):
    answer = 0
    prime_nums = [i for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if prime_nums[i] == 0:
            continue

        for j in range(i**2, n+1, i):
            prime_nums[j] = 0
        
    print([i for i in prime_nums[2:] if prime_nums[i]])

    return answer



if __name__ == "__main__":
    answer = solution(33)
    print(answer)