# lv 2. 짝지어 제거하기
def solution(s):
    """
    짝지어 제거해서 모든 문자열이 제거 가능하면 1을 반환하고 아니면 0을 반환
    """
    """i=0
    stack=[]
    
    stack.append(i)
    
    # 원래 코드는 문자열을 실제로 업데이트 시켜서 아예 처음부터 loop을 돌도록 함.
    # stack을 활용하는데 굳이 이렇게 할 이유가 없었음. -> stack이 뭔가 stack의 역할을 다 못한 느낌..?
    # 애초에 문제 정의부터 좀 잘못되었던 것 같다.
    # 이렇게 되면 최악의 경우 1+...+n으로 O(n^2)의 시간복잡도를 가졌을 듯. (n: 문자열 길이)
    
    while i < len(s)-1:
        i += 1
        top = stack.pop()
        
        if s[top] == s[i]: # 짝지어 있는 경우
            s = s[:top]+s[i+1:]
            i = 0
            stack.append(i)
        
        else: # 짝지어 있지 않은 경우
            stack.append(i)
    
    if len(s)==0: # 짝지어서 제거가 된 경우
        return 1
    else:
        return 0"""
    
    stack = []
    
    for c in s: # 한 번만 탐색하기 때문에 O(n)에 끝낼 수 있음.
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return int(stack == [])