# 다른사람 풀이!! 시간 빠름
# 내 풀이는 1300ms인데 이 풀이는 332ms

N, M = map(int, input().split())

board = []
wall = []
cctv = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 6:
            wall.append((i,j))
        elif line[j] != 0:
            cctv.append((i,j,line[j]))
    board.append(line)
# t r b l
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def cctv_act_direction(x,y, direction) -> list[tuple]:
    result = []
    while True:
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x >= N or y < 0 or y >= M:
            return result
        if board[x][y] == 6:
            return result
        elif board[x][y] in [1,2,3,4,5]:
            continue
        else:
            result.append((x,y))

# traveled -> list[tuple]
def cctv_act(x,y, num, traveled):
    result = []
    if num == 1:
        for i in range(4):
            new_traveled = traveled + cctv_act_direction(x,y,i)
            new_traveled = list(set(new_traveled))
            if new_traveled not in result:
                result.append(new_traveled)
    elif num == 2:
        for i in range(2):
            new_traveled = traveled + cctv_act_direction(x,y,i) + cctv_act_direction(x,y,i+2)
            new_traveled = list(set(new_traveled))
            if new_traveled not in result:
                result.append(new_traveled)
    elif num == 3:
        for i in range(4):
            new_traveled = traveled + cctv_act_direction(x,y,i) + cctv_act_direction(x,y,i-1)
            new_traveled = list(set(new_traveled))
            if new_traveled not in result:
                result.append(new_traveled)
    elif num == 4:
        for i in range(4):
            new_traveled = traveled + cctv_act_direction(x,y,i) + cctv_act_direction(x,y,i-1) + cctv_act_direction(x,y,i-2)
            new_traveled = list(set(new_traveled))
            if new_traveled not in result:
                result.append(new_traveled)
    else:
        new_traveled = []
        for i in range(4):
            new_traveled += cctv_act_direction(x,y,i)
            new_traveled += traveled
        new_traveled = list(set(new_traveled))
        if new_traveled not in result:
            result.append(new_traveled)
    
    return result

total = [[]]

for cc in cctv:
    temp = []
    for i in range(len(total)):
        temp.extend(cctv_act(cc[0],cc[1], cc[2], total[i]))
    total = temp

cctv_count = len(cctv)
wall_count = len(wall)

global_min = N*M
for i in total:
    square = N*M - cctv_count - wall_count - len(i)
    if global_min > square:
        global_min = square

print(global_min)