from collections import deque
import sys 

input = sys.stdin.readline 

N, K = map(int, input().split())

# 만약 동생이 수빈이의 왼쪽에 있다면 걷기로만 이동 가능
if K<=N:
    print(N-K)
# 동생이 수빈이의 오른쪽에 있는 경우
else:
    point = [1e9] * 100001

    q = deque()
    q.append((N, 0))
    point[N] = 0

    while q:
        x, time = q.popleft()

        # 순간이동할 수 있는 경우 (2*x)
        # 100000 < 2^18
        for i in range(1, 18):
            idx = x*(2**i)
            if idx > 100000:
                break
            if point[idx] > time:
                point[idx] = time
                q.append((idx, time))

        # 걷기
        if x-1>= 0 and point[x-1] == 1e9:
            point[x-1] = time+1
            q.append((x-1, time+1))

        if x+1 < 100001 and point[x+1] == 1e9:
            point[x+1] = time+1
            q.append((x+1, time+1))

    print(point[K])