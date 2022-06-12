# 괄호 짝 맞추기 -> 스택 풀이
def solution(s):
    answer = True
    pair = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    stack = []
    
    for char in s:
        if not stack:
            stack.append(char)
            continue
        
        if stack[-1] not in pair.keys(): # 닫힌 괄호로 시작하게 되면 무조건 False
            return False
        
        if pair[stack[-1]] == char:
            stack.pop()
        
        else:
            stack.append(char)

    
    return stack == []