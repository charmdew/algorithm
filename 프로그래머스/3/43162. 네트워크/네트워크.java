import java.util.*;

class Solution {
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<n; i++){
            graph.add(new ArrayList<Integer>());
        }
        
        for(int i=0; i<n;i++){
            for(int j=0; j<n; j++) {
                if(i==j) continue;
                
                if(computers[i][j]==1){
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        
        // 방문 여부 저장
        boolean[] visited = new boolean[n];
        
        Queue<Integer> q = new LinkedList<>();
        
        int x;
        for(int i=0; i<n; i++){
            if(visited[i]) continue;
            
            answer++;
            
            visited[i] = true;
            q.add(i);
            while(q.size()>0){
                x = q.poll();
                
                for(Integer to: graph.get(x)){
                    if(visited[to]) continue;
                    
                    visited[to] = true;
                    q.add(to);
                }
            }
            q.clear();
        }

        return answer;
    }
}