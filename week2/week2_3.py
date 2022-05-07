# 빙고 (lv.3)

def solution(board, nums):
    """
    set 자료형은 해시테이블로 구현되어 있기 때문에 O(1) 시간에 탐색이 가능함.
    
    원래는 list 자료형인 nums에서 board[row][col]을 찾았기 때문에, O(n^3)의 시간복잡도를 가졌음.
    그러나, nums를 set 자료형으로 변경함으로써 O(n^2)의 시간복잡도를 가지며 코드 효율 개선.
    """
    answer = 0
    n = len(board)
    nums = set(nums)
    
    
    # before
    ## bottleneck in this code : O(n^3)
    """
    for row in range(n):
        for col in range(n):
            if board[row][col] in nums:
                board[row][col] = 0
    """
    
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
     
    return answer


def solution2(board, nums):
    """
    zip(*board) -> 이런 식으로 하면 column-wise하게 묶을 수 있음.
    """
    answer = 0
    n = len(board)
    nums = set(nums)
    
    for row in range(n):
        for col in range(n):
            if board[row][col] in nums:
                board[row][col] = 0
                
	# horizontal (각 행을 탐색하면서 sum = 0인지 체크)
    answer += len([i for i in board if sum(i)==0])
    # vertical (각 열을 탐색하면서 sum = 0인지 체크)
    answer += len([i for i in zip(*board) if sum(i)==0])
    # diagonal (대각요소의 합이 0인지 체크)
    answer += int(sum(board[i][i] for i in range(n))==0)
    # off-diagonal
    answer += int(sum(board[n-i-1][i] for i in range(n))==0)
    
    return answer