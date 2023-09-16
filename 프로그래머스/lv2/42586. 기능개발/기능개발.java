import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();
        
        int length = progresses.length;
        System.out.println(length);
        
        // 배포되기까지 며칠이 걸리는지 구하기
        int[] cost = new int[length];
        for(int i=0; i<length; i++){
            cost[i] = (100-progresses[i]) / speeds[i];
            if((100-progresses[i]) % speeds[i] != 0) {
                cost[i]++;
            }
        }
        
        // 앞에 있는 기능이 며칠 후에 배포되는지, 각 배포마다 몇개의 기능이 배포되는지 
        int pre = cost[0], cnt = 1;
        for(int i=1; i<length; i++){
            if(pre >= cost[i]) {
                cnt++;
                continue;
            }
            result.add(cnt);
            pre = cost[i];
            cnt = 1;
        }
        result.add(cnt);
        
        int[] answer = result.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
}