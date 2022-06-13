def solution(brown, red):
    """
    red의 가로 세로를 어떻게 설정할 것인지에 따라 경우의 수가 나뉨.
    가로, 세로는 red의 약수로 구할 수 있음.
    """
    answer = []
    red_cands = get_divisor(red)          
    for cand in red_cands:
        if (sum(cand)*2 + 4) == brown:
            answer = [cand[0]+2, cand[1]+2]
    return answer

def get_divisor(n):
    """
    에라토스테네스의 체 알고리즘은 약수를 구할 때에도 효율적으로 구할 수 있게 해줌.
    """
    arr = []
    end = int(n**(1/2))
    for i in range(1,end+1):
        if n % i == 0:
            arr.append((n//i, i))
    
    return arr