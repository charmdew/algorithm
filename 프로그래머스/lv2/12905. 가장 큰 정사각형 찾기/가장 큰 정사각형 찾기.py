def solution(board):
    answer = 1234

    m = board[0][0]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
                m = max(m, board[i][j])
                
    answer = m**2
    
    return answer