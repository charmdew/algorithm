# 큐를 사용해서 (행, 열, 거리)를 저장한 후 bfs 돌려서 치킨거리를 구하면 시간초과 뜸..

from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 도시의 정보 입력
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 정보 저장
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
            # city[i][j] = 0  # 빈칸으로 변경
        elif city[i][j] == 1:
            home.append((i, j))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 도시의 치킨거리 최솟값 구하기
answer = 1e9

# 치킨집 중에 M개 선택
for case in combinations(chicken, M):

    # 치킨 거리 계산
    city_dist = 0

    # 집과 치킨집 사이 거리 계산
    for hx, hy in home:
        chicken_dist = 1e9
        # case에 담긴 치킨집 표시
        for cx, cy in case:
            dist = abs(hx-cx) + abs(hy-cy)
            chicken_dist = min(chicken_dist, dist)

        city_dist += chicken_dist

    answer = min(answer, city_dist)

print(answer)