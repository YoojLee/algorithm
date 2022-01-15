# 운송 트럭

def solution(max_weight, specs, names):
    """
    각 트럭은 운송 가능한 최대 weight이 존재함. 각 물품의 중량과 물품 목록이 주어졌을 때 몇 대의 트럭이 운송에 필요한지?
    """
    answer = 1 # 처음부터 한 대의 트럭은 필요하므로
    specs_dict = dict()
    for name, weight in specs:
        specs_dict[name] = int(weight)

    sum_weight = 0
    
    for i in range(len(names)):
        sum_weight += specs_dict[names[i]]
        if sum_weight > max_weight: # 최대 중량을 넘겼을 때
            answer += 1
            sum_weight = specs_dict[names[i]]
     
    return answer