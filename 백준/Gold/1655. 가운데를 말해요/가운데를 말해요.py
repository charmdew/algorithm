# 2개의 힙 사용
# 하나는 최대힙(작은 수 저장), 하나는 최소힙(큰 수 저장)
# 각 단계마다 최대힙에서 가장 큰수를 출력하면 그 수가 중간값!

import sys
import heapq

input = sys.stdin.readline

N = int(input())

maxHeap, minHeap = [], []

for _ in range(N):
    x = int(input())

    # 만약 첫번째 수라면 최대힙에 저장
    if not maxHeap:
        heapq.heappush(maxHeap, -x)
        print(x)
        continue

    l, r = -maxHeap[0], minHeap[0] if minHeap else 1e9
    # 최대힙, 최소힙에 있는 수와 현재 정수 비교
    if r < x:
        # 최대힙, 최소힙 크기가 1이라면
        if len(maxHeap) < len(minHeap):
            # 최소힙에 있는 수 최대힙으로 이동
            n = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -n)
        # 최소힙에 숫자 추가
        heapq.heappush(minHeap, x)
    else:
        if len(maxHeap) > len(minHeap):
            if -maxHeap[0] > x:
                # 최대힙에 있는 수 최소힙으로 이동
                n = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -n)
                heapq.heappush(maxHeap, -x)
            else:
                heapq.heappush(minHeap, x)
        else:
            # 최대힙에 숫자 추가
            heapq.heappush(maxHeap, -x)
    # 최소힙의 크기가 더 크면 최소힙 값 출력, 아니면 최대힙 값 출력
    print(minHeap[0] if len(maxHeap) < len(minHeap) else -maxHeap[0])

"""
5
4
0
3
1
2

4
0
3
1
2
"""