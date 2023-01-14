import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    target = y - x

    result = 0

    start, end = 0, 2**30
    while True:
        mid = (start + end) // 2

        # 범위 확인
        if (mid-1)**2 + (mid-1) < target <= mid**2:
            result = 2*mid - 1
            break
        elif mid ** 2 < target <= mid**2 + mid:
            result = 2*mid
            break

        elif target <= (mid-1)**2 + (mid-1):
            end = mid

        elif target > mid**2 + mid:
            start = mid

    print(result)