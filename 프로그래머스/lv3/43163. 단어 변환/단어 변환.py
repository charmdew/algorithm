visited = [False] * 50
step = 1e9

def dfs(begin, target, words, n, l, cnt):
    global step
    
    if begin==target:
        # step.append(cnt)
        step= min(step, cnt)
    
    for i in range(n):
        # 이미 변환된 적이 있는 단어라면
        if visited[i]:
            continue
        
        # 한 개의 알파벳만 차이나야함
        diff = 0
        for j in range(l):
            if begin[j]!= words[i][j]:
                diff += 1
        
        # print("차이나는 알파벳 개수",  diff, words[i])
        
        if diff == 1:        
            visited[i] = True
            dfs(words[i], target, words, n, l, cnt+1)
            visited[i] = False
    

def solution(begin, target, words):
    answer = 0
    
    n = len(words)
    l = len(words[0])
    
    if target in words:
        dfs(begin, target, words, n, l, 0)
    
        answer = step
    
    return answer