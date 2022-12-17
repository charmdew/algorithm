class Solution {
    public String solution(int[] food) {
        String answer = "0";
        
//         int num = food.length-1;
        
//         // 반복 횟수 저장
//         int cnt = 0;
//         // 더할 문자열 저장
//         String addStr = "";
        
//         // 큰 수부터 시작
//         for(int i=food.length-1; i>0; i-- ){
//             cnt = food[i]/2; // 반복 횟수
//             addStr = ((num--)+"").repeat(cnt); // 더할 문자열
            
//             // 앞 뒤에 문자열 붙이기
//             answer = addStr +answer+ addStr;
//         }
        
        // ===================================
        // 간단한 풀이
        for (int i = food.length - 1; i > 0; i--) {
            for (int j = 0; j < food[i] / 2; j++) {
                answer = i + answer + i; // 자동 형변환 됨!
            }
        }
        
        return answer;
    }
}