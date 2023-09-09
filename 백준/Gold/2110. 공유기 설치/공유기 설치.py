# 이분탐색 사용!!!
# 가장 왼쪽에 있는 위치부터 순서대로 간격이 x이상이 되도록 공유기를 설치해 보면서 C개 이상을 설치할 수 있는지 확인

"""
최대를 집의 마지막 위치로 두면 안되는 경우 발생함..
2 2
0 
1
답:1 / 오답:0
"""

import sys

input = sys.stdin.readline

N, C = map(int, input().split())

router = [int(input()) for _ in range(N)]
router.sort()

# 가장 인접한 두 공유기 사이의 최대 거리 저장
dist = 0

s, e = 0, int(1e9)
while s <= e:
    x = (s+e)//2

    # 설치한 공유기 개수
    cnt = 1

    pre = router[0]
    # 왼쪽 위치부터 순서대로 간격이 x 이상이 되도록 공유기 설치
    for i in range(1, N):
        if router[i]-pre >= x:
            pre = router[i]
            cnt += 1

    # 설치된 개수가 C 이상인지 확인
    if cnt >= C:
        dist = x
        # x 늘려보기
        s = x+1
    else:
        e = x-1

print(dist)