def solution(dirs):
    move = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    path = []   # 경로 저장
    
    x, y = 0, 0 # 시작위치 (0, 0)
    for d in dirs:
        dx, dy = move[d]
        nx = x+ dx
        ny = y+ dy
        
        # 범위를 벗어나는 경우
        if nx<-5 or 5<nx or ny<-5 or 5<ny:
            continue
        
        # 경로 (양방향)
        way1 = (x, y, nx, ny)
        way2 = (nx, ny, x, y)
        
        if way1 not in path:
            path.append(way1)
            path.append(way2)
    
        x, y = nx, ny
    
    answer = len(path)//2
    
    return answer