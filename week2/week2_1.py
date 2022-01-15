# 직사각형의 각 꼭지점 중 나머지 한 점의 좌표 구하기 (세 점이 주어졌을 때)
from collections import Counter

def solution(v):
    answer = []

    x = [x for x, _ in v]
    y = [y for _, y in v]
    
    answer += [key for key, value in Counter(x).items() if value == 1] # extend처럼 기능하는 듯?
    answer += [key for key, value in Counter(y).items() if value == 1]

    return answer