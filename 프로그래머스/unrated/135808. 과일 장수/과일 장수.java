import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        // 사과 점수 오름차순 정렬
        Arrays.sort(score);
        
        // 최저 사과 점수
        int lowScore;
        
        for(int i=score.length; i-m>-1; i=i-m){
            
            lowScore = score[i-m];

            // (최저 사과 점수) * (한 상자에 담긴 사과 개수) 더하기
            answer += lowScore * m;
        }
        
        return answer;
    }
}