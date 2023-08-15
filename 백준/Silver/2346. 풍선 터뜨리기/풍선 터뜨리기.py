import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

q = deque()

for i in range(N):
    q.append((i+1, nums[i]))  # (번호, 값)

result = []
while q:
    # print(q)
    idx, next = q.popleft()
    result.append(idx)
    # 오른쪽
    if next > 0:
        q.rotate(-next+1)

    # 왼쪽
    else:
        q.rotate(-next)


print(*result)