def solution(board, nums):
    """
    일단 nums 부분을 다 다른 값으로 대체해버리고 board 내에서 dfs 때려버리기..?
    -> 무조건 한 방향으로만 탐색 루트를 정리를 해버려야할 것 같음 대신.
    -> dfs 방법도 내일 해보기
    """
    answer = 0
    n = len(board)
    
    for row in range(n):
        for col in range(n):
            if board[row][col] in nums:
                board[row][col] = 0
    
    # 오른쪽으로 이동 (horizontal 빙고)
    for i in range(n):
        for j in range(n-1):
            if board[i][j] != board[i][j+1]:
                break
        else:
            answer += 1
            
    # 아래로 이동 (vertical 빙고)
    for i in range(n):
        for j in range(n-1):
            if board[j][i] != board[j+1][i]:
                break
        else:
            answer += 1
    
    # diagonal
    for i in range(n-1):
        if board[i][i] != board[i+1][i+1]:
            break
    else:
        answer += 1
        
    
    # off-diagonal
    for i in range(n-1):
        if board[i][n-1-i] != board[i+1][n-1-(i+1)]:
            break
    else:
        answer += 1
                         
                
    """
    # 각 빙고 방향에 대해서 다 룰베이스를 때려버린다.
    answer += len([i for i in board if sum(i) == 0]) # horizontal
    answer += len([i for i in zip(*board) if sum(i) == 0]) # vertical (이렇게 하면 vertical이 되는 게 더 신기함)
    answer += int(sum(board[i][i] for i in range(n)) == 0) # diagonal
    answer += int(sum(board[n - 1 - i][i] for i in range(n)) == 0) # off-diagonal
    """        
    return answer