class Solution {
    public int[] solution(int n) {
        int cnt = n*(n+1)/2;
        
        int[] answer = new int[cnt];
        int[][] result = new int[n][n];
        
        // 아래, 오른쪽, 대각선
        int[] dx = {1, 0, -1};
        int[] dy = {0, 1, -1};
        
        // 현재 위치
        int x = -1, y = 0;
        
        int num = 1;
        
        // 달팽이 배열 채우기 (아래, 오른쪽, 대각선 순으로)
        for(int i=0; i<n; i++){
            for(int k=0; k<n-i; k++){
                x += dx[i%3];
                y += dy[i%3];
                result[x][y] = num++;
            }
        }
        
        int idx = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<i+1; j++){
                answer[idx++] = result[i][j];
            }
        }
        
        return answer;
    }
}