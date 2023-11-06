def solution(plans):
    answer = []
    
    n = len(plans)
    # 시작시각, 걸리는 시간, 이름 순으로 정보 저장
    for i in range(n):
        name, start, playtime = plans[i]
        plans[i] = [int(start[:2])*60+int(start[3:]), int(playtime), name]
    plans.sort()
    
    
    # 잠시 멈춰둔 과제 [남은 시간, 이름]
    stop = []
    
    # 최근 과제 종료 시각
    end = plans[0][0]+plans[0][1]
    
    for i in range(n):
        start, playtime, name = plans[i]
        
        # 이전 과제를 끝내고 다음 과제까지 시간이 남는다면
        if end < start:
            # 잠시 멈춰둔 과제 수행
            while stop:
                remain, st_name = stop.pop()
                
                if end + remain > start:
                    stop.append([end+remain-start, st_name])
                    end = end + remain - start
                    break
                    
                # 과제 끝
                answer.append(st_name)
                end += remain
                
        # 과제를 끝내기 전 다음 과제 시작
        if i < n-1 and start+playtime > plans[i+1][0]:  
            stop.append([start+playtime-plans[i+1][0], name])
            end = plans[i+1][0]
        
        # 과제 모두 수행
        else:
            answer.append(name)
            end = start+playtime
    
    # 멈춰둔 과제 중 최근 멈춘 과제부터 끝냄
    while stop:
        remain, st_name = stop.pop()
        answer.append(st_name)
    
    return answer