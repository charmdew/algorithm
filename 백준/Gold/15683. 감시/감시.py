import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

room_info = [list(map(int, input().split())) for _ in range(N)]
room = [[room_info[i][j] for j in range(M)] for i in range(N)]

# CCTV 위치, 사각지대 영역 수
camera_pos, blind_cnt, blind_spot = [], 0, 0
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            camera_pos.append((i, j))
        if room[i][j] == 0:
            blind_cnt += 1


def up(cx, cy):  # 위
    global N, M, blind_spot

    for x in range(cx-1, -1, -1):
        # 벽인 경우 끝
        if room[x][cy] == 6:
            break

        # 감시 영역이거나 다른 cctv 카메라 있는 경우 넘어감
        if room[x][cy] == '#' or 0 < room[x][cy] < 6:
            continue

        # 사각지대 감소
        room[x][cy] = '#'
        blind_spot -= 1


def down(cx, cy):  # 아래
    global N, M, blind_spot

    for x in range(cx+1, N):
        # 벽인 경우 끝
        if room[x][cy] == 6:
            break

        # 감시 영역이거나 다른 cctv 카메라 있는 경우 넘어감
        if room[x][cy] == '#' or 0 < room[x][cy] < 6:
            continue

        # 사각지대 감소
        room[x][cy] = '#'
        blind_spot -= 1


def left(cx, cy):  # 왼쪽
    global N, M, blind_spot

    for y in range(cy-1, -1, -1):
        # 벽인 경우 끝
        if room[cx][y] == 6:
            break

        # 감시 영역이거나 다른 cctv 카메라 있는 경우 넘어감
        if room[cx][y] == '#' or 0 < room[cx][y] < 6:
            continue

        # 사각지대 감소
        room[cx][y] = '#'
        blind_spot -= 1


def right(cx, cy):  # 아래
    global N, M, blind_spot

    for y in range(cy+1, M):
        # 벽인 경우 끝
        if room[cx][y] == 6:
            break

        # 감시 영역이거나 다른 cctv 카메라 있는 경우 넘어감
        if room[cx][y] == '#' or 0 < room[cx][y] < 6:
            continue

        # 사각지대 감소
        room[cx][y] = '#'
        blind_spot -= 1


def cctv_1(d, x, y):
    global N, M, blind_spot

    if d == 0:
        right(x, y)
    elif d == 1:
        down(x, y)
    elif d == 2:
        left(x, y)
    else:
        up(x, y)


def cctv_2(d, x, y):
    global N, M, blind_spot

    if d == 0:
        left(x, y)
        right(x, y)
    elif d == 1:
        up(x, y)
        down(x, y)
    else:
        return


def cctv_3(d, x, y):
    global N, M, blind_spot

    if d == 0:
        up(x, y)
        right(x, y)
    elif d == 1:
        right(x, y)
        down(x, y)
    elif d == 2:
        down(x, y)
        left(x, y)
    else:
        left(x, y)
        up(x, y)


def cctv_4(d, x, y):
    global N, M, blind_spot

    if d == 0:
        left(x, y)
        up(x, y)
        right(x, y)
    elif d == 1:
        up(x, y)
        right(x, y)
        down(x, y)
    elif d == 2:
        right(x, y)
        down(x, y)
        left(x, y)
    else:
        down(x, y)
        left(x, y)
        up(x, y)


def cctv_5(d, x, y):
    global N, M, blind_spot

    if d == 0:
        left(x, y)
        right(x, y)
        down(x, y)
        up(x, y)
    else:
        return


# 사각 지대의 최소 크기
answer = 64


n = len(camera_pos)
for case in product(range(4), repeat=n):
    # 사각지대 크기
    blind_spot = blind_cnt

    for i in range(n):
        r, c = camera_pos[i]

        if room[r][c] == 1:
            cctv_1(case[i], r, c)
        elif room[r][c] == 2:
            cctv_2(case[i], r, c)
        elif room[r][c] == 3:
            cctv_3(case[i], r, c)
        elif room[r][c] == 4:
            cctv_4(case[i], r, c)
        else:
            cctv_5(case[i], r, c)

    # for i in range(N):
    #     print(*room[i])
    # print(blind_spot)
    answer = min(answer, blind_spot)

    # 사무실 정보 초기화
    room = [[room_info[i][j] for j in range(M)] for i in range(N)]

print(answer)