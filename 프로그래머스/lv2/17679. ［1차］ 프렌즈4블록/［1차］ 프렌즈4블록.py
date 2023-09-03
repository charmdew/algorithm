def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    # finish가 True인 경우 게임 종료
    finish = False
    
    while not finish:
        finish = True
        
        # 각 열마다 지워지는 블록 인덱스 저장
        cnt = [set() for _ in range(n)]
        
        for i in range(m-1):
            for j in range(n-1):
                # 블록이 없는 위치는 넘어감
                if board[i][j] == 0:
                    continue
                
                # 4블록 같은지 확인
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]     :
                    # 지워질 인덱스 저장
                    cnt[j].update([i, i+1])
                    cnt[j+1].update([i, i+1])
                    
                    # 지워질 블록이 있는 경우 finish는 False
                    finish = False
        
        # 블록 지우기
        for j in range(n):
            answer += len(cnt[j])
            for i in cnt[j]:
                board[i][j] = 0
                
        # 지운 블록 정보를 저장할 리스트
        nboard = [[0]*n for _ in range(m)]
        
        # 블록 떨어뜨리기
        for j in range(n):
            idx = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != 0:
                    nboard[idx][j] = board[i][j]
                    idx -= 1
        board = nboard

    return answer