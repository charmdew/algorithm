import sys

input = sys.stdin.readline

N, L = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 가로방향 길 확인
for r in range(N):
    # 경사로 놓였는지 저장
    slope = [[False]*N for _ in range(N)]
    # 길을 지나갈 수 있는지 여부
    go = True
    pre, cnt = maps[r][0], 1
    for c in range(1, N):
        if pre == maps[r][c]:
            cnt += 1

        # 이전 칸과 높이 차이가 1일때
        elif pre == maps[r][c]-1:
            # 이전에 L개의 연속된 값이 안 나오면 경사로 놓을 수 없음
            if cnt < L:
                go = False
                break
            # L개의 연속된 이전 칸 중 경사로가 놓여있으면 안됨
            for x in range(L):
                if slope[r][c-1-x]:
                    go = False
                    break

            cnt = 1
            pre = maps[r][c]
        # 이전 칸과 높이 차이가 1일때
        elif pre == maps[r][c]+1:
            slope[r][c] = True
            # L개의 연속된 칸 확인
            for j in range(c+1, c+L):
                # 경계를 벗어나거나 값이 다른 경우
                if j >= N or maps[r][c] != maps[r][j]:
                    go = False
                    break
                slope[r][j] = True
            if not go:
                break

            pre = maps[r][c]
            cnt = 0
            c += (L-1)

        else:
            go = False
            break

    if go:
        # print("가로방향", r)
        answer += 1


# 세로방향 길 확인
for c in range(N):
    # 경사로 놓였는지 저장
    slope = [[False]*N for _ in range(N)]
    # 길을 지나갈 수 있는지 여부
    go = True
    pre, cnt = maps[0][c], 1

    for r in range(1, N):
        if pre == maps[r][c]:
            cnt += 1

        # 이전 칸과 높이 차이가 1일때
        elif pre == maps[r][c]-1:
            # 이전에 L개의 연속된 값이 안 나오면 경사로 놓을 수 없음
            if cnt < L:
                go = False
                break
            # L개의 연속된 이전 칸 중 경사로가 놓여있으면 안됨
            for x in range(L):
                if slope[r-1-x][c]:
                    go = False
                    break

            cnt = 1
            pre = maps[r][c]
        # 이전 칸과 높이 차이가 1일때
        elif pre == maps[r][c]+1:
            slope[r][c] = True
            # L개의 연속된 칸 확인
            for i in range(r+1, r+L):
                # 경계를 벗어나거나 값이 다른 경우
                if i >= N or maps[r][c] != maps[i][c]:
                    go = False
                    break
                slope[i][c] = True
            if not go:
                break

            pre = maps[r][c]
            cnt = 0
            r += (L-1)

        else:
            go = False
            break

    if go:
        # print("세로방향", c)
        answer += 1

print(answer)