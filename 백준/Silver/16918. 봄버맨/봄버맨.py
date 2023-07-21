import sys 

input = sys.stdin.readline 

R, C, N = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            board[i][j] = 0

for t in range(2, N+1):
    if t % 2 == 0:
        # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
        for i in range(R):
            for j in range(C):
                if board[i][j] == '.':
                    board[i][j] = t

    else:
        # 업데이트 정보 저장
        nboard = [[board[i][j] for j in range(C)] for i in range(R)]
        
        # 3초 전에 설치된 폭탄이 모두 폭발함
        for r in range(R):
            for c in range(C):
                # 폭탄이 없거나 시간이 남은 경우는 넘어감
                if board[r][c]=='.' or board[r][c]+3 > t:
                    continue
                
                # 폭탄이 있던 칸 파괴
                nboard[r][c] = '.'

                # 상하좌우
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    # 경계 체크
                    if nr < 0 or nr >= R or nc < 0 or nc>= C:
                        continue
                
                    # 인접한 칸 파괴함
                    nboard[nr][nc] = '.'

        board = [[nboard[i][j] for j in range(C)] for i in range(R)]

# 폭탄 있는 곳 표시
for i in range(R):
    for j in range(C):
        if board[i][j] != '.':
            board[i][j] = 'O'

for i in range(R):
    print("".join(board[i]))