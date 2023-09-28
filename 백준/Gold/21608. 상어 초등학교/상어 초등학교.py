# 상어 초등학교
"""
자리를 정하는 방법
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
2. 1을 만족하는 칸이 여러 개이면 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정함
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

학생의 만족도
- 자리 배치가 모두 끝난 후 구할 수 있음
- 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수 (n)
    n == 0 : 0
    n > 0 : 10**(n-1)

출력 : 학생의 만족도의 총 합
"""

N = int(input())

# 좋아하는 학생 리스트 저장
st = [[] for _ in range(N**2+1)]

# 반 (0: 비어있는 상태)
room = [[0]*(N+1) for _ in range(N+1)]

# 비어있는 칸
blank = list(range(1, N**2+1))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 자리 정하기
def seat(num):
    global N

    # 자리 후보
    cand = []

    # 비어있는 칸 확인
    for b in blank:
        # 비어있는 칸 위치
        r = (b+(N-1))//N        # 행
        c = b%N if b%N else N   # 열

        # 좋아하는 학생 수, 비어있는 칸 수
        l_cnt, b_cnt = cnt(r, c, st[num])

        cand.append([l_cnt, b_cnt, b])

    # 1. 좋아하는 학생 수(내림차순)
    # 2. 비어있는 칸 수(내림차순)
    # 3. 칸 번호 (오름차순)
    # 정렬한 후 가장 첫번째 원소가 들어갈 자리다!
    cand.sort(key=lambda x:[-x[0],-x[1],x[2]])
    pos = cand[0][2]

    # 비어있는 칸 제거
    blank.remove(pos)

    return pos


# 인접한 칸에 좋아하는 학생이 몇 명 있는지
def cnt(x, y, like):
    global N
    c = 0   # 좋아하는 학생 수
    b = 0   # 비어있는 칸 수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나는 경우
        if 0>=nx or nx>N or 0>=ny or ny>N:
            continue

        # 좋아하는 학생인 경우
        if room[nx][ny] in like:
            c += 1
        # 비어있는 칸인 경우
        elif room[nx][ny] == 0:
            b += 1
    return (c, b)

for _ in range(N**2):
    info = list(map(int, input().split()))

    st_num = info[0]
    st[st_num] = info[1:]

    # 자리 구하기
    pos = seat(st_num)
    # print(st_num, pos)

    # 자리 배치
    r = (pos + (N - 1)) // N  # 행
    c = pos % N if pos % N else N  # 열
    room[r][c] = st_num


ans = 0
# 학생 만족도 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        x = cnt(i, j, st[room[i][j]])
        # 학생의 수가 0보다 크면
        if x[0]>0:
            ans += 10 ** (x[0]-1)

print(ans)