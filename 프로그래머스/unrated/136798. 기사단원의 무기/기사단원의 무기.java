class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        // 1의 약수 개수
        answer+=1;
        
        for(int i=2; i<=number; i++){
            int cnt = 0;
            
            // 약수 개수 구하기
            for (int j = 1; j * j <= i; j++) {
                if (j * j == i) cnt++;
                else if (i % j == 0) cnt += 2;
            }

            // 제한수치가 넘어간다면
            if(cnt>limit) cnt = power;
            
            answer += cnt;
        }
        
        return answer;
    }
}