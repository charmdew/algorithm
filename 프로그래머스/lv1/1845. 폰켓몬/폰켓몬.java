import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
   
        // the length of nums array
        int N = nums.length;
        
        HashMap<Integer, Integer> phoneketmon = new HashMap<>();
        for(int i=0; i<N; i++){
            // System.out.println(i);
            int cnt = 0;
            if(phoneketmon.containsKey(nums[i])){
                cnt = phoneketmon.get(nums[i]);
            }
            phoneketmon.put(nums[i], cnt+1);
        }
        
        // size
        int size = phoneketmon.size();
        
        answer = Math.min(size, N/2);
        
        return answer;
    }
}