def solution(s):
    answer = len(s)
    
    # 완전 탐색
    for step in range(1, len(s)+1): # step은 실제로 문자열 길이의 반이 최대임. (그 이후로는 압축이 무의미하기 때문)
        compressed = ''
        arr = []
        
        for start in range(0, len(s), step):
            end = start + step
            sliced = s[start:end]

            if start == 0:
               arr.append(sliced)
                
            else:
                if arr[-1] != sliced: # 중복 문자열을 체크하는 것이기 때문에 0이어도 무관
                    if len(arr) == 1:
                        compressed += f'{arr[-1]}'
                    else:
                        compressed += f'{len(arr)}{arr[-1]}'
                    arr = [] # arr flushing
                
                arr.append(sliced)
        
        if arr: # 배열이 비어있지 않다면
            if len(arr) == 1:
                compressed += f'{arr[-1]}'
            else:
                compressed += f'{len(arr)}{arr[-1]}'
        
        answer = min([len(compressed), answer])
    
    return answer