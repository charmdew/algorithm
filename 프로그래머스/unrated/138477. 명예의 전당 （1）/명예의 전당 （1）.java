import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        
        // 우선순위 큐 사용
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int i=0, len=score.length; i<len; i++){
            if(pq.size()<k){
                pq.add(score[i]);
            } else{
                // 명예의 전당에서 최하위 점수
                int x = pq.poll();
                
                // 더 큰 값 명예의 전당에 올리기
                pq.add(x<score[i]? score[i]: x);
            }
            
            // 명예의 전당의 최하위 점수 저장
            answer[i] = pq.peek();
        }
        
        return answer;
    }
}