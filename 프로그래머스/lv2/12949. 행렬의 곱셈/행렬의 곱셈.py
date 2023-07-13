def solution(arr1, arr2):    
    # 행렬 arr1 : r1 * c1
    # 행렬 arr2 : r2 * c2 (r2 = c1)
    # arr1&arr2 곱한 행렬 : r1 * c2 
    
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    answer = [[0]*c2 for _ in range(r1)]
    
    for r in range(r1):
        for c in range(c2):
            # 행렬곱의 결과 구하기
            mul = 0
            for x in range(c1):
                mul += (arr1[r][x]*arr2[x][c])
            
            answer[r][c] = mul
    
    return answer