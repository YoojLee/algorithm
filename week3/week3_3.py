# 주사위게임
from collections import defaultdict
def solution(monster, S1, S2, S3):
    answer = 0
    count_dict = defaultdict(int)
    
    # O(S1*S2*S3)의 시간복잡도
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                count_dict[i+j+k+1] += 1 # 이동 후 위치를 key값으로

    for state in count_dict:
        if state not in monster:
            answer += count_dict[state]

    return int(1000*(answer / (S1*S2*S3)))