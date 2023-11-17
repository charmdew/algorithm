import java.util.*;

class Solution {
    
    class Position {
        int x;
        int y;
        
        Position(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    
    public int solution(int[][] maps) {
        int answer = -1;
        
        // 상하좌우
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        int n = maps.length;
        int m = maps[0].length;
        
        int INF = 10001;
        
        int[][] dist = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                dist[i][j] = INF;
            }
        }
        
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(0, 0));
        dist[0][0] = 1;
        
        Position pos;
        int nx; int ny;
        while(q.size()>0){
            pos = q.poll();
            
            // 상하좌우 이동
            for(int i=0; i<4; i++){
                nx = pos.x + dx[i];
                ny = pos.y + dy[i];
                
                // 경계 벗어나면 무시
                if (nx < 0 || nx >= n || ny < 0 || ny >= m){
                    continue;
                }
                
                // 목표 지점에 도달한 경우
                if (nx == n-1 && ny == m-1){
                    answer = dist[pos.x][pos.y] + 1;
                    return answer;
                }
                
                // 벽인 경우 안됨
                if (maps[nx][ny] == 0){
                    continue;
                }
                
                // 이미 방문한 곳인 경우 안됨
                if (dist[nx][ny] < INF){
                    continue;
                }
                
                dist[nx][ny] = dist[pos.x][pos.y]+1;
                q.add(new Position(nx, ny));
                    
            }
        }
        
        return answer;
    }
}