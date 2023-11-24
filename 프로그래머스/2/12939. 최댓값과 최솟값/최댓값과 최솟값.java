import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr = s.split(" ");
        
        // 최댓값
        int max = Integer.parseInt(arr[0]);
        // 최솟값
        int min = Integer.parseInt(arr[0]);
        
        int x;
        for(int i=1; i<arr.length; i++){
            x = Integer.parseInt(arr[i]);
            if(max < x) {
                max = x;
            }
            if (min > x) {
                min = x;
            }
        }
        
        answer = min + " " + max;
        
        return answer;
    }
}