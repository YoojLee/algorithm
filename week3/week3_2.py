from itertools import combinations
def solution(m, weights):
    """
    m 그램을 담을 수 있는 가방에 사탕을 가득 채우는 경우의 수.
    같은 사탕은 또 넣을 수 없음.
    가방을 정확히 m 그램으로 채우는 경우의 수를 return
    
    완전 탐색을 해야할 거 같은데..? -> weights의 길이가 매우 짧기 때문에 가능했던 코드.
    """
    answer = 0
    for n in range(len(weights)):
        comb = combinations(weights, n)
        for c in comb:
            if sum(c) == m:
                answer += 1

    return answer