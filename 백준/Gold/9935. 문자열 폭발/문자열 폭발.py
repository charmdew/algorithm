import sys

input = sys.stdin.readline

in_str = input().rstrip()
bomb = input().rstrip()
l = len(bomb)
stack = []

for x in in_str:
    stack.append(x)
    if len(stack)>=l and ''.join(stack[len(stack)-l:]) == bomb:
        for i in range(l):
            stack.pop()

print(''.join(stack) if len(stack)>0 else "FRULA")