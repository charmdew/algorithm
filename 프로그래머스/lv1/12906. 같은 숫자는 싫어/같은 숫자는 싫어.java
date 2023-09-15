import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        int pre = -1;
        for(int x: arr){
            // 연속적으로 나타나는 숫자 넘어감
            if (pre == x) {
                continue;
            }
            list.add(x);
            pre = x;
        }
        
        // Integer ArrayList를 int 배열로 변환
        int[] answer = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        
        return answer;
    }
}