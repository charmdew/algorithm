import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String, Boolean> phone_map = new HashMap<>();
        
        for(String phone_num: phone_book){
            for(int i=0; i<phone_num.length()-1; i++){
                String key = phone_num.substring(0, i+1);
                // System.out.println(key); 
                
                phone_map.put(key, true);
            }
        }
        
        for(String phone_num: phone_book){
            if(phone_map.containsKey(phone_num)){
                answer = false;
                break;
            }
        }
        
        return answer;
    }
}