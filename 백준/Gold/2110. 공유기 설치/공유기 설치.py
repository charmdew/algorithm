# 이분탐색 사용!!!
# 다른 사람 풀이 
import sys
input = sys.stdin.readline

N, C = map(int,input().split())
wifi = sorted([int(input()) for _ in range(N)])

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = wifi[-1] - wifi[0]
answer = 0
binary_search(wifi,start,end)
print(answer)