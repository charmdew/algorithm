import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int max = 0;
                
        int[] cnt = {0, 0, 0};
        for(int i=0; i<answers.length; i++){
            if(answers[i] == one[i%one.length]){
                cnt[0] += 1;
                if (cnt[0] > max){
                    max = cnt[0];
                }
            } if(answers[i] == two[i%two.length]){
                cnt[1] += 1;
                if (cnt[1] > max){
                    max = cnt[1];
                }
            } if(answers[i] == three[i%three.length]){
                cnt[2] += 1;
                if (cnt[2] > max){
                    max = cnt[2];
                }
            } 
        }
        
        List<Integer> ans = new ArrayList<Integer>();
        for(int i=0; i<3; i++){
            if(cnt[i]==max){
                ans.add(i+1);
            }
        }
        
        // ArrayList -> int 배열
        answer = ans.stream()
                .mapToInt(i -> i)
                .toArray();
        
        return answer;
    }
}