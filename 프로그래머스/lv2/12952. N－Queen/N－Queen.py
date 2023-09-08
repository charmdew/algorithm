answer = 0

# row : 이번에 퀸을 놓을 행 위치
# queens: 지금까지 놓인 퀸의 위치 리스트
def nqueen(row, queens, n):
    global answer
    
    # row가 n이라면 조건을 만족하도록 배치할 수 있는 경우임!
    if row == n:
        answer += 1
        return
    
    # 열에 하나씩 놓아보고 가능한지 확인
    for c in range(n):
        # 퀸이 서로를 공격할 수 없는지 여부
        possible = True
        for qx, qy in queens:
            # 열이 같거나 대각선에 존재한다면 불가능 
            if qy == c or abs(row-qx) == abs(c-qy):
                possible = False
                break
        # 퀸을 놓을 수 있는 위치라면
        if possible:
            nqueen(row+1, queens + [(row, c)], n)

def solution(n):
    global answer
    
    # 퀸의 시작점 설정(n가지)
    for c in range(n):
        nqueen(1, [(0, c)], n)

    return answer