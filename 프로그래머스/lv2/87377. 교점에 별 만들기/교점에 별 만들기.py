# INF 범위 설정 잘 안해주면 테스트 27, 28 실패함..

from itertools import combinations

def solution(line):
    INF = 1e11
    
    # 교점 저장
    point = set()
    
    min_x, min_y, max_x, max_y = INF, INF, -INF, -INF
    
    # 직선 중에서 2개를 고르는 모든 경우
    cases = combinations(line, 2)
    for case in cases:
        # 직선1 : Ax + By + E = 0
        # 직선2 : Cx + Dy + F = 0
        A, B, E = case[0]
        C, D, F = case[1]
        
        # 두 직선이 평행 또는 일치하면 교점 X
        if A*D == B*C:
            continue
        
        # 두 직선 사이의 교점 (x, y)
        x = (B*F-E*D)/(A*D-B*C)
        y = (E*C-A*F)/(A*D-B*C)
        
        int_x, int_y = (B*F-E*D)//(A*D-B*C), (E*C-A*F)//(A*D-B*C)
        # 교점 (x, y)가 정수인 경우
        if x-int_x==0 and y-int_y==0:
            min_x = min(min_x, int_x)
            max_x = max(max_x, int_x)
            min_y = min(min_y, -int_y)
            max_y = max(max_y, -int_y)
            
            point.add((int_x, -int_y))
            
    # 행 크기 : max_y-min_y+1
    # 열 크기 : max_x-min_x+1
    N = max_y-min_y+1 
    M = max_x-min_x+1

    answer = [['.']*M for _ in range(N)]
    for p in point:
        answer[p[1]-min_y][p[0]-min_x] = '*'
    for i in range(N):
        answer[i] = ''.join(answer[i])
            
    return answer