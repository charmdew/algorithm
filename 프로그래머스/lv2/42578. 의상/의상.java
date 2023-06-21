import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> clothes_map = new HashMap<>();
        
        int N = clothes.length;
        
        for(int i=0; i<N; i++){
            int cnt = 0;
            if(clothes_map.containsKey(clothes[i][1])){
                cnt = clothes_map.get(clothes[i][1]);
            }
            clothes_map.put(clothes[i][1], cnt+1);
        }
        
        for(String kind: clothes_map.keySet()){
            answer *= (clothes_map.get(kind)+1);
        }
        
        answer -= 1;
        
        return answer;
    }
}