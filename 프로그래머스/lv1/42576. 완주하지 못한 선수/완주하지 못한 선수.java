import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        int N = participant.length;
        
        HashMap<String, Integer> part = new HashMap();
        for(int i=0; i<N; i++){
            int cnt = 0;
            if(part.containsKey(participant[i])){
                cnt = part.get(participant[i]);
            }
            part.put(participant[i], cnt+1);
        }
        
        for(int i=0; i<N-1; i++){
            int cnt = part.get(completion[i]);
            
            if(cnt-1 == 0){
                part.remove(completion[i]);
                continue;
            } 
            part.put(completion[i], cnt-1);
        }
        
        for(String key: part.keySet()){
            answer = key;
        }
    
        return answer;
    }
}