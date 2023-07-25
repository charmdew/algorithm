import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# 거꾸로 T를 S로 바꿀 수 있는지 판단
# T -> S
# 1. A 빼기
# 2. 문자열 뒤집고 B 제거
possible = 0


def transfer(x):
    global possible

    if x == '':
        return

    # print(x)
    if x == S:
        possible = 1
        return

    # 1. A 빼기
    if x[-1] == 'A':
        transfer(x[:-1])

    # 2. 문자열 뒤집고 B 제거
    x = x[::-1]
    if x[-1] == 'B':
        transfer(x[:-1])


transfer(T)
print(possible)