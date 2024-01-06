def solution(board, h, w):
    answer = 0
    
    n = len(board)
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if h_check < 0 or h_check >= n or w_check < 0 or w_check >= n:
            continue

        if board[h_check][w_check] == board[h][w]:
            answer += 1

    return answer