# N-Queen
def solution(n):
    """
    2차원 board로 구현할 경우, 시간 초과가 발생함.
    조건에 맞게 queen을 배치하고자 할 경우를 따져보면, board를 굳이 2차원으로 구현할 필요가 없음.
    
    서로 공격하지 못하게 하려면 각 열과 각 행에 무조건 queen이 하나씩 배치되는 형태로 구성되기 때문임. 
    따라서 따져야할 경우의 수가 훨씬 줄어들게 됨.
    """
    arr = [0, 0]

    def dfs(board, cur_row):
        if cur_row == n:
            if arr[0] == n:
                arr[1] += 1
            return

        # O(n^2)으로 탐색
        for j in range(n): # O(n)
            board[cur_row] = j
            if check(board, cur_row): # O(n)
                arr[0] += 1
                dfs(board, cur_row+1)
                arr[0] -= 1

        return


    def check(board, i):
        """
        - Args
            board: 1차원 배열로 구현된 체스판
            i: 주어진 위치의 row (배열 인덱스: row, 배열 값: col; 즉, 배열 인덱스로 column에 접근 가능함)
        """
        for row in range(i): # 뒤에 놓여있는 것보다 앞에 있는 것만 고려하면 됨.
            if (board[i] == board[row]) or (abs(board[i]-board[row]) == i-row):
                return False

        return True


    dfs([0 for _ in range(n)], 0)
        
    return arr[1]

if __name__ == "__main__":
    n = 5
    print(solution(n))