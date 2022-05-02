# 사전순 부분 문자열
def solution(s):
    """
    모든 부분 문자열을 만들 필요가 있을까?
    문자의 순서는 뒤바꾸지 않는다고 했으니까 그냥 처음부터 문자열 끝까지 순차적으로 탐색하면 될 것 같음.
    그러니까 그냥 stack을 쓰는데 모든 부분 문자열 말고 하나하나 greedy하게 담아내는 것..??
    예를 들면 하나 일단 집어넣고 뒤에 거랑 비교하면서 사전 순으로 뒤에 있으면 넣고 아님 빼기?
    
    -> 하지만, 위와 같은 경우에는 aava 같이 하면 안되더라.. v 만났을 때 앞의 a밖에 안지워지니까...
    새로운 친구를 만났다면 바로 앞의 값이랑만 비교하면 안되고 전체를 다 비교하는 게 중요함.
    """
    stack = []
    
    for i, char in enumerate(s):
        while stack and stack[-1] < char: # stack이 비어있지 않고 stack[-1]이 char보다 작다면
            stack.pop() # stack에 있는 거 다 pop
        stack.append(char) # 이 명령을 수행할 때는 stack은 당연히 비어있을 것임. 그때는 그럼 당연히 stack에 append해줘야,
           
    return "".join(stack)