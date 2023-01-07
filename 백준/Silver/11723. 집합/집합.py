import sys

input = sys.stdin.readline

M = int(input())

S = 0
for _ in range(M):
    command = input().split()
    if len(command)>1:
        x = int(command[1])

    if command[0]=="add":
        x -= 1
        # S에 x 추가
        S = S | (1<<x)
    elif command[0] == "remove":
        x -= 1
        # S에 x 제거
        S = S & ~(1 << x)
    elif command[0] == "check":
        x -= 1
        # S에 x가 있으면 1, 없으면 0 출력
        print((S & (1 << x)) >> x)
    elif command[0] == "toggle":
        x -= 1
        if (S & (1 << x)) >> x:
            S = S & ~(1 << x)
        else:
            S = S | (1 << x)
    elif command[0] == "all":
        S = 0b11111111111111111111
    elif command[0]=="empty":
        S = 0