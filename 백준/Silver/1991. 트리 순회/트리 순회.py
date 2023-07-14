# dfs 활용하기!
import sys

# 전위순회
def preorder(x):
    if x=='.':
        return

    # 루트
    print(x, end='')
    
    left, right = btree[x]
    # 왼쪽 자식
    preorder(left)
    # 오른쪽 자식
    preorder(right)


# 중위순회
def inorder(x):
    if x=='.':
        return
    
    left, right = btree[x]
    # 왼쪽 자식
    inorder(left)

    # 루트
    print(x, end='')

    # 오른쪽 자식
    inorder(right)

# 후위순회
def postorder(x):
    if x=='.':
        return
    
    left, right = btree[x]
    # 왼쪽 자식
    postorder(left)
    # 오른쪽 자식
    postorder(right)

    # 루트
    print(x, end='')

input = sys.stdin.readline

# 노드의 개수 N 입력
N = int(input())

# 이진 트리 정보 저장
btree = dict()
for _ in range(N):
    node, left, right = input().split()

    btree[node] = (left, right)

# 항상 A가 루트 노드가 됨
preorder('A')
print()
inorder('A')
print()
postorder('A')