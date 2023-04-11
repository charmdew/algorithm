def solution(sequence, k):
    answer = [0, 1e9]
    
    N = len(sequence)
    s = 0
    
    sum_seq = 0
    
    for i in range(N):
        sum_seq += sequence[i]
            
        if sum_seq == k and (i-s) < (answer[1]-answer[0]):
            print(i, sum_seq)
            answer = [s, i]
            continue
        
        if sum_seq < k:
            continue
        
        while sum_seq > k:
            sum_seq -= sequence[s]
            s += 1
        
        if sum_seq == k and (i-s) < (answer[1]-answer[0]):
            answer = [s, i]
            
    return answer